import pandas as pd
df = pd.read_csv("raw.csv", dtype=str, keep_default_na=False)
print("rows", len(df), "exact dups", df.duplicated().sum(), "dup ids", df.lead_id.duplicated().sum())
for c in df.columns:
    s = df[c]
    print(f"\n== {c}: blanks={(s.str.strip()=='').sum()} unique={s.nunique()}")
    if c not in ("lead_id","created_date","deal_value_eur"):
        print(s.value_counts().head(25).to_string())
d = df.created_date
print("\ndate formats:", d.str.replace(r"\d","9",regex=True).value_counts().to_string())
v = df.deal_value_eur
print("\ndeal formats:", v.str.replace(r"\d","9",regex=True).value_counts().head(15).to_string())
print("\ndeal by stage nonblank:", df[v!=""].stage.value_counts().to_string())
print("\nnon-L ids:", df[~df.lead_id.str.match(r"^L\d+$")].to_string())
print(pd.crosstab(df.source.str.lower().str.strip(), df.campaign).to_string())
