#!/usr/bin/env python3
"""
Sample size for a two-variant test on a rate (reply rate, meeting rate, CTR).

Usage:
    python sample_size.py --baseline 0.03 --mde 0.02 [--relative] \
        [--alpha 0.05] [--power 0.8] [--weekly-volume 300]

--baseline       current rate of the primary metric (0.03 = 3%)
--mde            smallest lift worth detecting. Absolute points by default
                 (0.02 = +2 points), or relative with --relative (0.5 = +50%)
--weekly-volume  contacts or impressions you can send per week across both variants

Prints n per variant, total, and weeks needed. If the answer is unrealistic,
the honest options are: test a bigger difference, use a higher-volume metric,
or pool across segments.
"""
import argparse
import math
from statistics import NormalDist


def n_per_variant(p1, p2, alpha=0.05, power=0.8):
    z_a = NormalDist().inv_cdf(1 - alpha / 2)
    z_b = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2
    num = (z_a * math.sqrt(2 * p_bar * (1 - p_bar)) + z_b * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / (p2 - p1) ** 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", type=float, required=True)
    ap.add_argument("--mde", type=float, required=True)
    ap.add_argument("--relative", action="store_true")
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--power", type=float, default=0.8)
    ap.add_argument("--weekly-volume", type=int)
    a = ap.parse_args()

    p1 = a.baseline
    p2 = p1 * (1 + a.mde) if a.relative else p1 + a.mde
    if not 0 < p1 < 1 or not 0 < p2 < 1:
        raise SystemExit("Rates must be between 0 and 1.")
    n = n_per_variant(p1, p2, a.alpha, a.power)
    print(f"Baseline {p1:.2%} -> target {p2:.2%} (lift {p2 - p1:+.2%} points, {(p2 / p1 - 1):+.0%} relative)")
    print(f"Alpha {a.alpha}, power {a.power}")
    print(f"Needed: {n:,} per variant, {2 * n:,} total")
    if a.weekly_volume:
        weeks = 2 * n / a.weekly_volume
        print(f"At {a.weekly_volume:,} per week: {weeks:.1f} weeks")
        if weeks > 8:
            print("That's over 8 weeks. Consider a bigger difference, a higher-volume metric, or pooling segments.")


if __name__ == "__main__":
    main()
