#!/usr/bin/env python3
"""
Read out an A/B experiment from a results CSV. All statistics run here, in code.

The CSV has one row per contact (or impression), a variant column, and 0/1
outcome columns, plus optional segment columns.

Usage:
    python readout.py results.csv --primary meeting_booked \
        --secondary replied positive_reply \
        --guardrails negative_reply unsubscribed \
        --segment segment --planned-n 600 --control A \
        [--expected-split 0.5] [--json out.json]

What it reports, per metric:
    rate per variant, absolute and relative lift, 95% interval on the lift,
    two-sided p-value (two-proportion z-test), and the probability that the
    challenger beats control (Beta(1,1) prior, Monte Carlo).

Checks it runs:
    sample ratio mismatch (is the split what was planned?)
    planned sample size reached?
    guardrail metrics significantly worse?
    segment consistency (does one segment drive the whole result?)
    small-numbers warning when a variant has fewer than 10 primary conversions
"""
import argparse
import json
import math
import sys

import numpy as np
import pandas as pd

Z95 = 1.959963984540054
RNG = np.random.default_rng(7)


def norm_sf(z):
    return 0.5 * math.erfc(z / math.sqrt(2))


def compare(xa, na, xb, nb):
    pa, pb = xa / na, xb / nb
    diff = pb - pa
    pooled = (xa + xb) / (na + nb)
    se_pooled = math.sqrt(pooled * (1 - pooled) * (1 / na + 1 / nb)) if 0 < pooled < 1 else 0
    p_value = 2 * norm_sf(abs(diff) / se_pooled) if se_pooled else 1.0
    se = math.sqrt(pa * (1 - pa) / na + pb * (1 - pb) / nb)
    lo, hi = diff - Z95 * se, diff + Z95 * se
    a = RNG.beta(1 + xa, 1 + na - xa, 200_000)
    b = RNG.beta(1 + xb, 1 + nb - xb, 200_000)
    return {
        "control_rate": pa, "challenger_rate": pb,
        "abs_lift": diff, "rel_lift": (diff / pa) if pa else float("nan"),
        "ci_low": lo, "ci_high": hi, "p_value": p_value,
        "prob_challenger_better": float((b > a).mean()),
        "control_conversions": int(xa), "challenger_conversions": int(xb),
    }


def srm(na, nb, expected=0.5):
    n = na + nb
    ea, eb = n * expected, n * (1 - expected)
    chi2 = (na - ea) ** 2 / ea + (nb - eb) ** 2 / eb
    p = math.erfc(math.sqrt(chi2 / 2))  # chi-square, 1 degree of freedom
    return chi2, p


def pct(x, d=1):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x * 100:.{d}f}%"


def pts(x):
    return f"{x * 100:+.1f} pts"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--variant", default="variant")
    ap.add_argument("--control", default="A")
    ap.add_argument("--primary", required=True)
    ap.add_argument("--secondary", nargs="*", default=[])
    ap.add_argument("--guardrails", nargs="*", default=[])
    ap.add_argument("--segment")
    ap.add_argument("--planned-n", type=int, help="Planned sample size per variant")
    ap.add_argument("--expected-split", type=float, default=0.5, help="Expected share in control")
    ap.add_argument("--json")
    a = ap.parse_args()

    df = pd.read_csv(a.csv)
    variants = df[a.variant].unique().tolist()
    if a.control not in variants or len(variants) != 2:
        sys.exit(f"Need exactly two variants including control '{a.control}'. Found: {variants}")
    chal = [v for v in variants if v != a.control][0]
    g = df.groupby(a.variant)
    n = g.size()
    na, nb = int(n[a.control]), int(n[chal])

    out = {"control": a.control, "challenger": chal, "n_control": na, "n_challenger": nb,
           "metrics": {}, "checks": {}, "segments": {}}
    for m in [a.primary] + a.secondary + a.guardrails:
        s = g[m].sum()
        out["metrics"][m] = compare(s[a.control], na, s[chal], nb)

    chi2, p_srm = srm(na, nb, a.expected_split)
    out["checks"]["srm_p"] = p_srm
    out["checks"]["planned_n"] = a.planned_n
    out["checks"]["planned_n_reached"] = (min(na, nb) >= a.planned_n) if a.planned_n else None
    prim = out["metrics"][a.primary]
    out["checks"]["small_numbers"] = min(prim["control_conversions"], prim["challenger_conversions"]) < 10
    out["checks"]["guardrails_breached"] = [
        m for m in a.guardrails
        if out["metrics"][m]["abs_lift"] > 0 and out["metrics"][m]["p_value"] < 0.05
    ]

    if a.segment:
        for seg, d in df.groupby(a.segment):
            sg = d.groupby(a.variant)
            sn = sg.size()
            if a.control in sn and chal in sn:
                ss = sg[a.primary].sum()
                out["segments"][str(seg)] = compare(ss[a.control], sn[a.control], ss[chal], sn[chal])
                out["segments"][str(seg)]["n"] = int(sn.sum())
        lifts = {k: v["abs_lift"] for k, v in out["segments"].items()}
        total_lift_x = prim["challenger_conversions"] / nb - prim["control_conversions"] / na
        out["checks"]["segments_disagree"] = any(np.sign(l) != np.sign(total_lift_x) for l in lifts.values() if l != 0)
        # share of the challenger's extra conversions that come from the single biggest segment
        extra = {}
        for k in out["segments"]:
            d = df[df[a.segment].astype(str) == k]
            c = d[d[a.variant] == chal][a.primary].sum() - d[d[a.variant] == a.control][a.primary].sum()
            extra[k] = int(c)
        tot = sum(v for v in extra.values() if v > 0)
        top = max(extra, key=extra.get) if extra else None
        out["checks"]["extra_conversions_by_segment"] = extra
        out["checks"]["top_segment_share_of_gain"] = (extra[top] / tot) if tot and top else None
        out["checks"]["top_segment"] = top

    # verdict
    p_better = prim["prob_challenger_better"]
    issues = []
    if p_srm < 0.01:
        issues.append("sample ratio mismatch: the split is not what was planned, so the randomisation may be broken")
    if out["checks"]["planned_n_reached"] is False:
        issues.append("planned sample size not reached")
    if out["checks"]["guardrails_breached"]:
        issues.append("guardrail worse: " + ", ".join(out["checks"]["guardrails_breached"]))
    if p_srm < 0.01 or out["checks"]["guardrails_breached"]:
        verdict = "DO NOT SHIP: fix the issue above first"
    elif out["checks"]["planned_n_reached"] is False:
        verdict = "KEEP RUNNING: planned sample not reached, don't call it early"
    elif p_better >= 0.95:
        verdict = f"SHIP {chal}"
    elif p_better <= 0.05:
        verdict = f"KEEP {a.control}: challenger is worse"
    else:
        verdict = "NO CLEAR WINNER: keep control, log the learning, test a bigger difference"
    out["verdict"], out["issues"] = verdict, issues

    # report
    L = []
    L.append(f"# Readout: {a.csv}\n")
    L.append(f"Control **{a.control}** (n={na:,}) vs challenger **{chal}** (n={nb:,})\n")
    L.append("| Metric | Role | Control | Challenger | Lift | 95% interval | p-value | P(challenger better) |")
    L.append("|---|---|---|---|---|---|---|---|")
    for m, r in out["metrics"].items():
        role = "primary" if m == a.primary else ("guardrail" if m in a.guardrails else "secondary")
        L.append(f"| {m} | {role} | {pct(r['control_rate'])} ({r['control_conversions']}) | "
                 f"{pct(r['challenger_rate'])} ({r['challenger_conversions']}) | {pts(r['abs_lift'])} "
                 f"({pct(r['rel_lift'], 0)} rel.) | {pts(r['ci_low'])} to {pts(r['ci_high'])} | "
                 f"{r['p_value']:.3f} | {pct(r['prob_challenger_better'])} |")
    L.append("\n## Checks\n")
    L.append(f"- Sample ratio: p = {p_srm:.3f} ({'OK' if p_srm >= 0.01 else 'MISMATCH'})")
    if a.planned_n:
        L.append(f"- Planned n per variant: {a.planned_n:,} ({'reached' if out['checks']['planned_n_reached'] else 'NOT reached'})")
    L.append(f"- Small numbers on primary metric: {'YES, fewer than 10 conversions in a variant, treat as directional' if out['checks']['small_numbers'] else 'no'}")
    L.append(f"- Guardrails breached: {', '.join(out['checks']['guardrails_breached']) or 'none'}")
    if a.segment:
        L.append(f"\n## Segments ({a.primary})\n")
        L.append("| Segment | n | Control | Challenger | Lift | P(challenger better) |")
        L.append("|---|---|---|---|---|---|")
        for k, r in out["segments"].items():
            L.append(f"| {k} | {r['n']:,} | {pct(r['control_rate'])} | {pct(r['challenger_rate'])} | {pts(r['abs_lift'])} | {pct(r['prob_challenger_better'])} |")
        share = out["checks"]["top_segment_share_of_gain"]
        if share is not None:
            L.append(f"\n- Extra conversions by segment (challenger minus control): {out['checks']['extra_conversions_by_segment']}")
            L.append(f"- {out['checks']['top_segment']} accounts for {pct(share, 0)} of the challenger's gain")
            if share > 0.6:
                L.append("- WARNING: one segment drives most of the result. Check before generalising it to everyone.")
        if out["checks"]["segments_disagree"]:
            L.append("- WARNING: at least one segment moves in the opposite direction.")
    L.append(f"\n## Verdict\n\n**{verdict}**")
    for i in issues:
        L.append(f"- {i}")
    print("\n".join(L))
    if a.json:
        with open(a.json, "w") as f:
            json.dump(out, f, indent=2, default=float)


if __name__ == "__main__":
    main()
