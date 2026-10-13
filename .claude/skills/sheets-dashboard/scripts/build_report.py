#!/usr/bin/env python3
"""
Build a presentable, self-contained HTML report from the same spec.json and
clean data used by build_dashboard.py.

Every number is calculated here with pandas, independently of the spreadsheet
formulas. If the report and the Sheet agree, both are right.

Usage:
    python build_report.py spec.json report.html [--sheet-url URL]

Optional spec keys used only by the report:
    "subtitle": "One line under the title"
    "question": "The question this analysis answers"
"""
import argparse
import html
import json
import math
from datetime import date
from pathlib import Path

import pandas as pd

FMT = {
    "int": lambda v: f"{v:,.0f}",
    "dec": lambda v: f"{v:,.2f}",
    "pct": lambda v: f"{v * 100:.1f}%",
    "eur": lambda v: f"€{v:,.0f}",
    "usd": lambda v: f"${v:,.0f}",
    "gbp": lambda v: f"£{v:,.0f}",
    "pln": lambda v: f"{v:,.0f} zł",
}


def fmt(v, kind="int"):
    if v is None or (isinstance(v, float) and (math.isnan(v) or math.isinf(v))):
        return "n/a"
    return FMT.get(kind, FMT["int"])(v)


def esc(s):
    return html.escape(str(s))


class Report:
    def __init__(self, spec, base):
        self.spec = spec
        self.clean = pd.read_csv(base / spec["clean_csv"])
        self.tables = {t["name"]: pd.read_csv(base / t["csv"]) for t in spec.get("extra_tables", [])}

    # ---- calculations ------------------------------------------------------
    def metric_series(self, m, gb, keys):
        agg = m.get("agg")
        if agg == "count":
            return self.clean.groupby(gb).size().reindex(keys).fillna(0)
        if agg == "sum":
            return self.clean.groupby(gb)[m["column"]].sum().reindex(keys).fillna(0)
        if agg == "lookup":
            t = self.tables[m["table"]]
            return t.groupby(m["key"])[m["column"]].sum().reindex(keys).fillna(0)
        raise SystemExit(f"Unknown agg in {m}")

    def breakdown(self, b):
        gb = b["group_by"]
        keys = [k for k in self.clean[gb].dropna().unique().tolist() if k not in b.get("exclude", [])]
        cols, totals = {}, {}
        for m in b["metrics"]:
            if "ratio" in m:
                a, d = m["ratio"]
                cols[m["label"]] = cols[a] / cols[d].where(cols[d] != 0)
                totals[m["label"]] = totals[a] / totals[d] if totals[d] else float("nan")
            else:
                s = self.metric_series(m, gb, keys)
                cols[m["label"]] = s
                totals[m["label"]] = s.sum()
        df = pd.DataFrame(cols)
        sort_by = b.get("sort_by")
        if sort_by in df:
            df = df.sort_values(sort_by, ascending=False)
        return df, totals

    def kpis(self):
        vals, out = {}, []
        for k in self.spec.get("kpis", []):
            if "ratio" in k:
                a, d = k["ratio"]
                v = vals[a] / vals[d] if vals.get(d) else float("nan")
            elif k.get("agg") == "count":
                v = len(self.clean)
            elif k.get("agg") == "sum":
                v = self.clean[k["column"]].sum()
            elif k.get("agg") == "sum_table":
                v = self.tables[k["table"]][k["column"]].sum()
            else:
                v = float("nan")
            vals[k["label"]] = v
            out.append((k["label"], fmt(v, k.get("format", "int"))))
        return out

    # ---- rendering ---------------------------------------------------------
    def bar_chart(self, title, series, kind, highlight):
        s = series.dropna()
        s = s[~s.isin([float("inf")])].sort_values(ascending=False)
        if s.empty:
            return ""
        best = None
        if highlight == "high_good":
            best = s.idxmax()
        elif highlight == "low_good":
            best = s[s > 0].idxmin() if (s > 0).any() else None
        vmax = float(s.max()) or 1.0
        row_h, label_w, value_w, width = 34, 210, 90, 760
        plot_w = width - label_w - value_w
        h = row_h * len(s) + 8
        rows = []
        for i, (k, v) in enumerate(s.items()):
            y = 4 + i * row_h
            w = max(2.0, plot_w * float(v) / vmax)
            is_best = k == best
            cls = "bar best" if is_best else "bar"
            tip = f"{k}: {fmt(v, kind)}" + (" (best)" if is_best else "")
            label = esc(k) + (" ◆" if is_best else "")
            rows.append(
                f'<g class="row" tabindex="0"><title>{esc(tip)}</title>'
                f'<rect class="hit" x="0" y="{y}" width="{width}" height="{row_h}"/>'
                f'<text class="lab{" strong" if is_best else ""}" x="{label_w - 12}" y="{y + row_h / 2}" '
                f'text-anchor="end" dominant-baseline="middle">{label}</text>'
                f'<rect class="{cls}" x="{label_w}" y="{y + 8}" width="{w:.1f}" height="{row_h - 16}" rx="4"/>'
                f'<text class="val" x="{label_w + w + 8:.1f}" y="{y + row_h / 2}" dominant-baseline="middle">'
                f"{esc(fmt(v, kind))}</text></g>"
            )
        note = '<p class="chart-note">◆ marks the best performer on this measure.</p>' if best is not None else ""
        return (
            f'<figure class="chart"><figcaption>{esc(title)}</figcaption>'
            f'<svg viewBox="0 0 {width} {h}" role="img" aria-label="{esc(title)}">'
            f'<line class="base" x1="{label_w}" x2="{label_w}" y1="0" y2="{h}"/>{"".join(rows)}</svg>{note}</figure>'
        )

    def table(self, b, df, totals):
        fmts = {m["label"]: m.get("format", "int") for m in b["metrics"]}
        head = "".join(f"<th>{esc(c)}</th>" for c in [b["group_by"].replace("_", " ").capitalize()] + list(df.columns))
        body = ""
        for k, row in df.iterrows():
            body += "<tr><td>" + esc(k) + "</td>" + "".join(f"<td>{esc(fmt(row[c], fmts[c]))}</td>" for c in df.columns) + "</tr>"
        foot = "<tr><td>Total</td>" + "".join(f"<td>{esc(fmt(totals[c], fmts[c]))}</td>" for c in df.columns) + "</tr>"
        return f'<div class="tablewrap"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody><tfoot>{foot}</tfoot></table></div>'

    def build(self, out, sheet_url=None):
        sp = self.spec
        notes = sp.get("notes", {})
        tiles = "".join(f'<div class="tile"><div class="tl">{esc(l)}</div><div class="tv">{esc(v)}</div></div>' for l, v in self.kpis())
        sections = ""
        for b in sp.get("breakdowns", []):
            df, totals = self.breakdown(b)
            ch = b.get("chart")
            chart = ""
            if ch and ch["metric"] in df:
                m = next(x for x in b["metrics"] if x["label"] == ch["metric"])
                chart = self.bar_chart(f"{ch['metric']}, {b['title'].lower()}", df[ch["metric"]], m.get("format", "int"), m.get("highlight"))
            sections += f'<section class="block"><h2>{esc(b["title"])}</h2>{chart}{self.table(b, df, totals)}</section>'

        def lst(key, title):
            items = notes.get(key) or []
            if not items:
                return ""
            return f'<div class="note"><h3>{esc(title)}</h3><ul>' + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul></div>"

        findings = notes.get("findings") or []
        hero = ""
        if findings:
            hero = '<section class="findings"><h2>What the data says</h2><ol>' + "".join(f"<li>{esc(f)}</li>" for f in findings) + "</ol></section>"
        question = f'<p class="q"><span>Question</span>{esc(sp["question"])}</p>' if sp.get("question") else ""
        sheet = f'<a class="btn" href="{esc(sheet_url)}">Open the live Google Sheet</a>' if sheet_url else ""
        page = TEMPLATE.format(
            title=esc(sp.get("title", "Report")),
            subtitle=esc(sp.get("subtitle", f"{len(self.clean):,} rows after cleaning")),
            question=question,
            sheet=sheet,
            tiles=tiles,
            findings=hero,
            sections=sections,
            next=lst("next_steps", "Recommended next steps"),
            caveats=lst("caveats", "What this data can't tell us"),
            cleaning=lst("cleaning", "What was cleaned and why"),
            date=date.today().isoformat(),
        )
        Path(out).write_text(page, encoding="utf-8")


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root {{
  --bg:#F6F4EF; --surface:#FFFFFF; --ink:#1C1F1E; --muted:#5B655F; --rule:#D9DED9;
  --brand:#12352B; --bar:#2E8B62; --accent:#C27A12; --tile:#ECEFEA;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#141917; --surface:#1B211E; --ink:#E8ECE9; --muted:#A3ADA7; --rule:#2E3632;
  --brand:#CFE5DA; --bar:#3AA174; --accent:#C98320; --tile:#222A26;
}} }}
:root[data-theme="dark"] {{
  --bg:#141917; --surface:#1B211E; --ink:#E8ECE9; --muted:#A3ADA7; --rule:#2E3632;
  --brand:#CFE5DA; --bar:#3AA174; --accent:#C98320; --tile:#222A26;
}}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--ink); font:400 16px/1.55 Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif; }}
.wrap {{ max-width:1040px; margin:0 auto; padding:40px 16px 64px; }}
header {{ border-bottom:1px solid var(--rule); padding-bottom:24px; margin-bottom:28px; }}
.eyebrow {{ font:500 12px/1 ui-monospace, "IBM Plex Mono", monospace; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); }}
h1 {{ font-size:clamp(28px,4vw,40px); line-height:1.1; letter-spacing:-.02em; margin:10px 0 8px; color:var(--brand); font-weight:650; }}
.sub {{ color:var(--muted); margin:0; }}
.q {{ margin:18px 0 0; font-size:17px; }} .q span {{ display:inline-block; margin-right:10px; font:500 11px/1 ui-monospace,monospace; text-transform:uppercase; letter-spacing:.08em; color:var(--muted); }}
.btn {{ display:inline-block; margin-top:18px; background:var(--brand); color:var(--bg); padding:10px 16px; border-radius:6px; text-decoration:none; font-weight:600; font-size:14px; }}
.tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:12px; margin-bottom:36px; }}
.tile {{ background:var(--tile); border-radius:8px; padding:16px 18px; }}
.tl {{ font:500 11px/1.2 ui-monospace,monospace; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); }}
.tv {{ font-size:28px; font-weight:650; letter-spacing:-.02em; margin-top:6px; color:var(--brand); font-variant-numeric:tabular-nums; }}
.findings {{ background:var(--surface); border:1px solid var(--rule); border-left:4px solid var(--accent); border-radius:8px; padding:20px 24px; margin-bottom:40px; }}
.findings h2 {{ margin-top:0; }} .findings li {{ margin:6px 0; }}
h2 {{ font-size:22px; letter-spacing:-.01em; color:var(--brand); margin:0 0 14px; font-weight:650; }}
h3 {{ font-size:16px; margin:0 0 8px; color:var(--brand); }}
.block {{ margin-bottom:48px; }}
.chart {{ margin:0 0 16px; background:var(--surface); border:1px solid var(--rule); border-radius:8px; padding:16px 16px 8px; }}
figcaption {{ font-weight:600; margin-bottom:8px; }}
svg {{ width:100%; height:auto; display:block; }}
.bar {{ fill:var(--bar); }} .bar.best {{ fill:var(--accent); }}
.base {{ stroke:var(--rule); stroke-width:1; }}
.hit {{ fill:transparent; }} .row:hover .hit, .row:focus .hit {{ fill:var(--tile); }}
.row:focus {{ outline:none; }}
.lab {{ font-size:13px; fill:var(--ink); }} .lab.strong {{ font-weight:700; }}
.val {{ font-size:13px; fill:var(--muted); font-variant-numeric:tabular-nums; }}
.chart-note {{ font-size:12px; color:var(--muted); margin:6px 0 4px; }}
.tablewrap {{ overflow-x:auto; border:1px solid var(--rule); border-radius:8px; background:var(--surface); }}
table {{ width:100%; border-collapse:collapse; font-size:14px; font-variant-numeric:tabular-nums; }}
th, td {{ padding:9px 12px; text-align:right; border-bottom:1px solid var(--rule); white-space:nowrap; }}
th:first-child, td:first-child {{ text-align:left; }}
th {{ font-size:12px; font-weight:600; color:var(--muted); background:var(--tile); }}
tfoot td {{ font-weight:700; border-bottom:0; }}
.notes {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:16px; }}
.note {{ background:var(--surface); border:1px solid var(--rule); border-radius:8px; padding:18px 20px; }}
.note ul {{ margin:0; padding-left:18px; }} .note li {{ margin:5px 0; font-size:15px; }}
footer {{ margin-top:40px; color:var(--muted); font-size:13px; border-top:1px solid var(--rule); padding-top:16px; }}
</style>
</head>
<body>
<div class="wrap">
<header>
  <div class="eyebrow">Marketing performance report</div>
  <h1>{title}</h1>
  <p class="sub">{subtitle}</p>
  {question}
  {sheet}
</header>
<div class="tiles">{tiles}</div>
{findings}
{sections}
<section class="block"><h2>Notes</h2><div class="notes">{next}{caveats}{cleaning}</div></section>
<footer>Generated {date} by the sheets-dashboard skill. Every figure is calculated in code from the cleaned data; the Google Sheet holds the same figures as live formulas.</footer>
</div>
</body>
</html>
"""


def main():
    p = argparse.ArgumentParser()
    p.add_argument("spec")
    p.add_argument("out")
    p.add_argument("--sheet-url")
    a = p.parse_args()
    spec_path = Path(a.spec)
    Report(json.loads(spec_path.read_text()), spec_path.parent).build(a.out, a.sheet_url)
    print(f"Built {a.out}")


if __name__ == "__main__":
    main()
