import pandas as pd, re
df = pd.read_csv("raw.csv", dtype=str, keep_default_na=False)
print("rows", len(df), "exact dups", df.duplicated().sum(), "dup lead_id", df.lead_id.duplicated().sum())
d = df[df.lead_id.duplicated(keep=False)].sort_values("lead_id")
print("dup ids that are NOT exact dups:", d[~d.duplicated(keep=False)].lead_id.unique())
for c in df.columns:
    s = df[c]
    print(f"\n--- {c}: blanks={(s.str.strip()=='').sum()} unique={s.nunique()}")
    if c not in ("lead_id","created_date"): print(s.value_counts().head(40).to_dict())
dt = df.created_date
pats = dt.str.replace(r"\d","9",regex=True).value_counts()
print("\ndate patterns", pats.to_dict())
print("examples", {p: dt[dt.str.replace(r'\d','9',regex=True)==p].head(4).tolist() for p in pats.index})
iso = pd.to_datetime(dt, format="%Y-%m-%d", errors="coerce")
print("iso range", iso.min(), iso.max())
dm = dt[dt.str.contains("/")]
print("slash first-part>12:", (dm.str.split("/").str[0].astype(int)>12).sum(), "second-part>12:", (dm.str.split("/").str[1].astype(int)>12).sum())
v = df.deal_value_eur[df.deal_value_eur!=""]
print("\ndeal non-float values:", v[pd.to_numeric(v, errors="coerce").isna()].tolist())
print("deal by stage:", df.assign(h=df.deal_value_eur!="").groupby("stage").h.agg(["sum","count"]).to_dict())
num = pd.to_numeric(v, errors="coerce"); print(num.describe())
# junk / test rows
for c in ["lead_id","campaign","first_asset","job_title","source"]:
    m = df[c].str.contains(r"test|dummy|xxx|asdf|sample|delete|internal|corvane", case=False)
    if m.any(): print("JUNK?", c, df[m].to_dict("records"))
print(df[~df.lead_id.str.match(r"^L\d{4}$")])
print("campaign x source:\n", pd.crosstab(df.campaign.replace("","(blank)"), df.source.str.lower()))
