#!/usr/bin/env python3
"""
SEO and web analytics analysis. All maths runs here.

  keywords   Semrush / Ahrefs keyword export -> cleaned, filtered, scored and bucketed
  ga4        GA4 landing page export -> cleaned, spam and tracking gaps removed, performance tables

Usage:
  python seo_analysis.py keywords semrush.csv --brand corvane \
      --exclude jobs careers cheap freelance wordpress salary \
      --clusters clusters.json --out analysis/seo

  python seo_analysis.py ga4 ga4.csv --out analysis/ga4

KEYWORDS
  Expected columns (names matched loosely): Keyword, Intent, Position, Search Volume,
  Keyword Difficulty, CPC, URL. Blank position = not ranking.

  Estimated clicks use a position click-through curve. This is an ASSUMPTION (industry
  averages vary by SERP features); state it in any report. Change CTR below if you have
  Search Console data, which is better.

  Buckets:
    Quick win    ranking 4 to 20, difficulty <= 60, commercial or informational
    Content gap  not ranking, difficulty <= 35
    Defend       ranking 1 to 3
    Long shot    difficulty >= 70
    Later        everything else
  Opportunity score = extra monthly clicks at target position x CPC x (1 - difficulty/100)
  (CPC is used as a proxy for commercial value, not a plan to buy the keyword.)

GA4
  Expected columns: Week or Date, Session default channel group, Session source / medium,
  Landing page, Sessions, Engaged sessions, Key events.
  Removes exact duplicates, flags spam (100+ sessions at under 5% engagement), '(not set)'
  pages, and weeks where total sessions fall below 50% of the median (probable tracking break,
  excluded from trend calculations, never silently).
"""
import argparse
import json
import re
from pathlib import Path

import pandas as pd

CTR = {1: .28, 2: .15, 3: .11, 4: .08, 5: .06, 6: .045, 7: .035, 8: .03, 9: .025, 10: .022}


def ctr(pos):
    if pd.isna(pos):
        return 0.0
    p = int(pos)
    if p in CTR:
        return CTR[p]
    if p <= 20:
        return 0.01
    return 0.003


def num(s):
    return pd.to_numeric(s.astype(str).str.replace(",", "").str.strip().replace({"": None, "n/a": None, "nan": None}), errors="coerce")


def find(df, *names):
    low = {c.lower().strip(): c for c in df.columns}
    for n in names:
        for k, c in low.items():
            if n in k:
                return c
    return None


def md_table(df, cols, fmt=None):
    fmt = fmt or {}
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, r in df.iterrows():
        out.append("| " + " | ".join(fmt.get(c, str)(r[c]) if c in fmt else str(r[c]) for c in cols) + " |")
    return "\n".join(out)


def keywords(a):
    raw = pd.read_csv(a.file, dtype=str).fillna("")
    log = [f"Rows in: {len(raw)}"]
    c = {k: find(raw, *v) for k, v in {
        "kw": ("keyword",), "intent": ("intent",), "pos": ("position",), "vol": ("volume",),
        "kd": ("difficulty", "kd"), "cpc": ("cpc",), "url": ("url",)}.items()}
    if not c["kw"] or not c["vol"]:
        raise SystemExit(f"Need at least Keyword and Search Volume columns. Found: {list(raw.columns)}")
    df = pd.DataFrame({
        "keyword": raw[c["kw"]].str.strip().str.lower(),
        "intent": raw[c["intent"]].str.strip().str.lower() if c["intent"] else "",
        "position": num(raw[c["pos"]]) if c["pos"] else float("nan"),
        "volume": num(raw[c["vol"]]),
        "difficulty": num(raw[c["kd"]]) if c["kd"] else float("nan"),
        "cpc": num(raw[c["cpc"]]) if c["cpc"] else 0.0,
        "url": raw[c["url"]].str.strip() if c["url"] else "",
    })
    before = len(df)
    df = df.drop_duplicates(subset="keyword", keep="first")
    log.append(f"Duplicates removed (case-insensitive): {before - len(df)}")
    log.append(f"Volume stored as text with commas, converted: {raw[c['vol']].str.contains(',').sum()}")
    miss_kd = df["difficulty"].isna().sum()
    log.append(f"Missing difficulty: {miss_kd} (treated as 50, flagged)")
    df["kd_missing"] = df["difficulty"].isna()
    df["difficulty"] = df["difficulty"].fillna(50)

    excluded = []
    if a.brand:
        m = df["keyword"].str.contains("|".join(map(re.escape, a.brand)))
        excluded.append(df[m].assign(reason="brand"))
        df = df[~m]
    if a.exclude:
        m = df["keyword"].str.contains(r"\b(?:" + "|".join(map(re.escape, a.exclude)) + r")\b")
        excluded.append(df[m].assign(reason="off-target audience"))
        df = df[~m]
    exc = pd.concat(excluded) if excluded else df.iloc[0:0]
    log.append(f"Excluded: {len(exc)} ({exc.groupby('reason').size().to_dict() if len(exc) else {}})")

    df["clicks_now"] = df.apply(lambda r: r.volume * ctr(r.position), axis=1)
    target = df["position"].apply(lambda p: 1 if (not pd.isna(p) and p <= 3) else 3)
    df["clicks_at_target"] = df["volume"] * target.map(ctr)
    df["extra_clicks"] = (df["clicks_at_target"] - df["clicks_now"]).clip(lower=0)
    df["opportunity"] = df["extra_clicks"] * df["cpc"] * (1 - df["difficulty"] / 100)

    def bucket(r):
        if not pd.isna(r.position) and r.position <= 3:
            return "Defend"
        if r.difficulty >= 70:
            return "Long shot"
        if not pd.isna(r.position) and 4 <= r.position <= 20 and r.difficulty <= 60:
            return "Quick win"
        if pd.isna(r.position) and r.difficulty <= 35:
            return "Content gap"
        return "Later"
    df["bucket"] = df.apply(bucket, axis=1)
    # Long shots keep their theoretical value for reference, but score zero: a plan
    # shouldn't rank keywords the site can't realistically win.
    df["opportunity_if_won"] = df["opportunity"]
    df.loc[df["bucket"] == "Long shot", "opportunity"] = 0.0

    df["cluster"] = "unclustered"
    if a.clusters:
        cl = json.loads(Path(a.clusters).read_text())
        for name, terms in cl.items():
            m = (df["cluster"] == "unclustered") & df["keyword"].str.contains("|".join(map(re.escape, terms)))
            df.loc[m, "cluster"] = name

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    df.sort_values("opportunity", ascending=False).to_csv(out / "keywords_scored.csv", index=False)
    exc.to_csv(out / "keywords_excluded.csv", index=False)

    cl = df.groupby("cluster").agg(keywords=("keyword", "count"), volume=("volume", "sum"),
                                   extra_clicks=("extra_clicks", "sum"), opportunity=("opportunity", "sum"),
                                   avg_kd=("difficulty", "mean")).sort_values("opportunity", ascending=False).reset_index()
    cl.to_csv(out / "clusters.csv", index=False)
    ranked = df[df["position"].notna() & (df["position"] <= 20) & (df["url"] != "")]
    cannib = ranked.groupby("cluster")["url"].nunique()
    cannib = cannib[(cannib > 1) & (cannib.index != "unclustered")]

    f0, f1 = (lambda x: f"{x:,.0f}"), (lambda x: f"{x:,.1f}")
    L = ["# Keyword analysis", "", "## Cleaning", ""] + [f"- {x}" for x in log]
    order = ["Quick win", "Content gap", "Defend", "Later", "Long shot"]
    bk = df.groupby("bucket").agg(keywords=("keyword", "count"), volume=("volume", "sum"),
                                  opportunity=("opportunity", "sum")).reindex(order).dropna().reset_index()
    L += ["", "## Buckets", "", md_table(bk, ["bucket", "keywords", "volume", "opportunity"], {"keywords": f0, "volume": f0, "opportunity": f0})]
    ls = df[df.bucket == "Long shot"]
    if len(ls):
        L += ["", f"Long shots (difficulty 70+) score zero: {', '.join(ls.keyword)}. Combined volume {ls.volume.sum():,.0f}, but not realistic to win soon."]
    for b in ["Quick win", "Content gap"]:
        top = df[df.bucket == b].sort_values("opportunity", ascending=False).head(10)
        L += ["", f"## Top {b.lower()}s", "", md_table(top, ["keyword", "intent", "position", "volume", "difficulty", "cpc", "extra_clicks", "opportunity", "url"],
              {"position": lambda x: "-" if pd.isna(x) else f"{x:.0f}", "volume": f0, "difficulty": f0, "cpc": lambda x: f"€{x:.2f}", "extra_clicks": f1, "opportunity": f0})]
    L += ["", "## Clusters", "", md_table(cl, ["cluster", "keywords", "volume", "extra_clicks", "opportunity", "avg_kd"],
          {"volume": f0, "extra_clicks": f1, "opportunity": f0, "avg_kd": f0})]
    L += ["", "## Possible cannibalisation (more than one URL ranking in a cluster)", ""]
    if len(cannib):
        for k in cannib.index:
            urls = ranked[ranked.cluster == k].groupby("url")["keyword"].apply(list).to_dict()
            L.append(f"- **{k}**: " + "; ".join(f"`{u}` ({len(v)} keywords)" for u, v in urls.items()))
    else:
        L.append("- none found")
    L += ["", "## Assumptions", "", "- Clicks use an average position click-through curve; real CTR depends on SERP features. Search Console data beats this.",
          "- Opportunity uses CPC as a proxy for commercial value. It ranks keywords; it isn't a revenue forecast.",
          "- Search volume is a tool estimate, not measured traffic."]
    (out / "keywords_report.md").write_text("\n".join(L))
    print("\n".join(L))


def ga4(a):
    raw = pd.read_csv(a.file, dtype=str).fillna("")
    c = {k: find(raw, *v) for k, v in {
        "week": ("week", "date"), "chan": ("channel group", "channel"), "src": ("source",),
        "page": ("landing page", "page"), "s": ("sessions",), "e": ("engaged",), "k": ("key event", "conversion")}.items()}
    if c["s"] == c["e"]:
        c["s"] = next(col for col in raw.columns if col.lower().strip() == "sessions")
    log = [f"Rows in: {len(raw)}"]
    before = len(raw)
    raw = raw.drop_duplicates()
    log.append(f"Exact duplicate rows removed: {before - len(raw)}")
    df = pd.DataFrame({"week": raw[c["week"]], "channel": raw[c["chan"]], "source": raw[c["src"]],
                       "page": raw[c["page"]], "sessions": num(raw[c["s"]]).fillna(0),
                       "engaged": num(raw[c["e"]]).fillna(0), "key_events": num(raw[c["k"]]).fillna(0)})
    log.append(f"Sessions stored as text with commas, converted: {raw[c['s']].str.contains(',').sum()}")

    src = df.groupby("source").agg(sessions=("sessions", "sum"), engaged=("engaged", "sum"))
    spam = src[(src.sessions >= 100) & (src.engaged / src.sessions < 0.05)].index.tolist()
    log.append(f"Spam sources removed (100+ sessions, under 5% engaged): {spam or 'none'} ({int(df[df.source.isin(spam)].sessions.sum()):,} sessions)")
    df = df[~df.source.isin(spam)]
    notset = df[df.page == "(not set)"].sessions.sum()
    log.append(f"'(not set)' landing page sessions: {int(notset):,} (kept in totals, excluded from page tables)")

    wk = df.groupby("week").sessions.sum()
    broken = wk[wk < 0.5 * wk.median()].index.tolist()
    log.append(f"Probable tracking breaks (week total under 50% of median): {broken or 'none'}")

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    df.to_csv(out / "ga4_clean.csv", index=False)

    def table(g):
        t = g.agg(sessions=("sessions", "sum"), engaged=("engaged", "sum"), key_events=("key_events", "sum")).reset_index()
        t["engagement_rate"] = t.engaged / t.sessions.where(t.sessions > 0)
        t["conversion_rate"] = t.key_events / t.sessions.where(t.sessions > 0)
        return t.sort_values("sessions", ascending=False)

    ok = df[~df.week.isin(broken)]
    by_ch = table(df.groupby("channel"))
    by_pg = table(df[df.page != "(not set)"].groupby("page"))
    org = table(df[(df.channel == "Organic Search") & (df.page != "(not set)")].groupby("page"))
    org_wk = ok[ok.channel == "Organic Search"].groupby("week").sessions.sum()
    n = min(4, len(org_wk) // 2)
    first, last = org_wk.iloc[:n].mean(), org_wk.iloc[-n:].mean()
    by_ch.to_csv(out / "by_channel.csv", index=False)
    by_pg.to_csv(out / "by_page.csv", index=False)

    pct = lambda x: "n/a" if pd.isna(x) else f"{x * 100:.1f}%"
    f0 = lambda x: f"{x:,.0f}"
    cols = ["sessions", "engagement_rate", "key_events", "conversion_rate"]
    fm = {"sessions": f0, "key_events": f0, "engagement_rate": pct, "conversion_rate": pct}
    L = ["# GA4 analysis", "", "## Cleaning", ""] + [f"- {x}" for x in log]
    L += ["", "## By channel", "", md_table(by_ch, ["channel"] + cols, fm)]
    L += ["", "## By landing page", "", md_table(by_pg, ["page"] + cols, fm)]
    L += ["", "## Organic search by landing page", "", md_table(org, ["page"] + cols, fm)]
    L += ["", "## Organic trend (tracking-break weeks excluded)", "",
          f"- First {n} weeks average: {first:,.0f} sessions a week; last {n} weeks: {last:,.0f} ({(last / first - 1) * 100:+.0f}%)"]
    L += ["", "## Assumptions and limits", "",
          "- Key events are GA4 conversions (form submissions), not SQLs. Join to the CRM before judging channel value.",
          "- GA4 attributes sessions by its own rules; compare with revops/attribution-model.md before reallocating budget.",
          "- Weeks flagged as tracking breaks are excluded from trends, not from totals. Confirm with whoever owns the tag."]
    (out / "ga4_report.md").write_text("\n".join(L))
    print("\n".join(L))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    k = sub.add_parser("keywords")
    k.add_argument("file")
    k.add_argument("--brand", nargs="*", default=[])
    k.add_argument("--exclude", nargs="*", default=[])
    k.add_argument("--clusters")
    k.add_argument("--out", default="analysis/seo")
    g = sub.add_parser("ga4")
    g.add_argument("file")
    g.add_argument("--out", default="analysis/ga4")
    a = ap.parse_args()
    keywords(a) if a.cmd == "keywords" else ga4(a)


if __name__ == "__main__":
    main()
