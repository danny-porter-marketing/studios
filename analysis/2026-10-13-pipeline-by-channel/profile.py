import pandas as pd, re, sys
d = sys.argv[1]
df = pd.read_csv(f"{d}/raw.csv", dtype=str, keep_default_na=False)
print("rows", len(df), "exact dups", df.duplicated().sum(), "dup lead_id", df.lead_id.duplicated().sum(),
      "dup id non-identical", df[df.lead_id.duplicated(keep=False)].drop_duplicates().lead_id.duplicated().sum())
for c in df.columns:
    s = df[c]; print(f"\n== {c}: blanks={(s.str.strip()=='').sum()} unique={s.nunique()}")
    if c not in ("lead_id","created_date","deal_value_eur"): print(s.value_counts().to_string())
dt = df.created_date
print("\ndate formats:", dt.map(lambda x: "ISO" if re.fullmatch(r"\d{4}-\d{2}-\d{2}",x) else "DMY/" if re.fullmatch(r"\d{2}/\d{2}/\d{4}",x) else "other:"+x).value_counts().to_string())
dv = df.deal_value_eur
print("deal value non-numeric:", dv[(dv!="") & ~dv.str.fullmatch(r"\d+(\.\d+)?")].tolist())
print("deal value by stage (non-blank):"); print(df.assign(h=dv!="").groupby("stage").h.agg(['sum','count']))
print("total-ish rows:", df[df.apply(lambda r: r.str.contains("total", case=False).any(), axis=1)])
print("campaign x source:"); print(pd.crosstab(df.campaign.replace("","(blank)"), df.source.str.lower().str.strip()).to_string())
