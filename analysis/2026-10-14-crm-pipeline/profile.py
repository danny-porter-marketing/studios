import pandas as pd, sys, re
d=sys.argv[1]
df=pd.read_csv(f"{d}/raw.csv",dtype=str,keep_default_na=False)
print("rows",len(df),"exact dups",df.duplicated().sum(),"dup Record IDs",df["Record ID"].duplicated().sum())
for c in df.columns:
    s=df[c]; print(f"\n== {c}: blanks={(s.str.strip()=='').sum()} unique={s.nunique()}")
    if c not in("Record ID","Company"): print(s.value_counts().head(40).to_string())
print("\nDate formats:",df["Create Date"].str.replace(r"\d","9",regex=True).value_counts().to_dict())
amt=df["Deal Amount"]; print("Amount non-plain:",amt[~amt.str.fullmatch(r"(\d+(\.\d+)?)?")].value_counts().to_dict())
print("Company dup counts top:",df["Company"].value_counts().head(5).to_dict())
for kw in ["test","Test","TEST","asdf","example","demo","xxx"]:
    m=df.apply(lambda r: kw in " ".join(r),axis=1); 
    if m.any(): print(kw, df[m].to_string())
sp=pd.read_csv(f"{d}/raw_spend.csv",dtype=str,keep_default_na=False)
print("\nspend rows",len(sp),"dups on month/channel/campaign:",sp.duplicated(["month","channel","campaign"]).sum())
print(sp[sp.duplicated(["month","channel","campaign"],keep=False)])
