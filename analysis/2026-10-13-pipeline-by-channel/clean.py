"""raw.csv + raw_spend.csv -> clean.csv, spend_by_channel.csv, spend_by_campaign.csv"""
import re, sys
from pathlib import Path
import pandas as pd

d = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent
df = pd.read_csv(d / "raw.csv", dtype=str, keep_default_na=False)
n0 = len(df)
df = df.drop_duplicates()
print(f"rows {n0} -> {len(df)} (dropped {n0 - len(df)} exact duplicates)")
assert df.lead_id.is_unique

CHANNEL = {
    "linkedin ads": "LinkedIn Ads", "linkedin": "LinkedIn Ads",
    "google ads": "Google Ads", "google ppc": "Google Ads",
    "organic search": "Organic Search", "seo": "Organic Search", "organic": "Organic Search",
    "outbound email": "Outbound Email", "outbound": "Outbound Email", "cold email": "Outbound Email",
    "events": "Events", "event": "Events", "conference": "Events",
    "partner referral": "Partner Referral", "partner": "Partner Referral", "referral": "Partner Referral",
}
key = df.source.str.strip().str.lower()
unmapped = sorted(set(key) - set(CHANNEL))
assert not unmapped, unmapped
print("source spellings mapped:", key.nunique(), "->", key.map(CHANNEL).nunique(), "channels;",
      "rows renamed:", (key.map(CHANNEL) != df.source).sum())
df.insert(2, "channel", key.map(CHANNEL))
df = df.drop(columns="source")

# dates: ISO or DD/MM/YYYY
iso = df.created_date.str.fullmatch(r"\d{4}-\d{2}-\d{2}")
dmy = df.created_date.str.fullmatch(r"\d{2}/\d{2}/\d{4}")
assert (iso | dmy).all()
parsed = pd.to_datetime(df.created_date.where(iso), format="%Y-%m-%d")
parsed = parsed.fillna(pd.to_datetime(df.created_date.where(dmy), format="%d/%m/%Y"))
first = df.created_date[dmy].str[:2].astype(int)
print(f"dates: {dmy.sum()} DD/MM/YYYY converted; {(first > 12).sum()} have day>12 (confirms DD/MM)")
df["created_date"] = parsed.dt.strftime("%Y-%m-%d")
df["month"] = parsed.dt.strftime("%Y-%m")
print("date range", df.created_date.min(), df.created_date.max())

df["campaign"] = df.campaign.str.strip().replace("", "(none)")
title = df.job_title.str.strip()
fixed_titles = {t.lower(): t for t in title if t != t.lower()}
df["job_title"] = title.str.lower().map(fixed_titles)
assert df.job_title.notna().all()
print("job titles recased:", (title != df.job_title).sum())
blank_region = (df.region.str.strip() == "").sum()
df["region"] = df.region.str.strip().replace("", "Unknown")
print("regions set to Unknown:", blank_region)

dv = df.deal_value_eur.str.strip()
text_money = dv.str.contains(r"[€,]")
print("deal values stored as text:", text_money.sum())
df["deal_value_eur"] = pd.to_numeric(dv.str.replace(r"[€,\s]", "", regex=True).replace("", None))

STAGES = ["Lead", "MQL", "SQL", "Opportunity", "Closed Won", "Closed Lost"]
assert set(df.stage) <= set(STAGES)
df["is_mql"] = df.stage.isin(STAGES[1:]).astype(int)
df["is_sql"] = df.stage.isin(STAGES[2:]).astype(int)
df["is_opp"] = df.stage.isin(["Opportunity", "Closed Won", "Closed Lost"]).astype(int)
df["is_won"] = (df.stage == "Closed Won").astype(int)
df["pipeline_value_eur"] = df.deal_value_eur.where(df.is_opp == 1, 0).fillna(0)
df["won_value_eur"] = df.deal_value_eur.where(df.is_won == 1, 0).fillna(0)
assert (df.deal_value_eur.notna() == (df.is_opp == 1)).all()
df = df.sort_values(["created_date", "lead_id"])
df.to_csv(d / "clean.csv", index=False)

sp = pd.read_csv(d / "raw_spend.csv", keep_default_na=False)
sp = sp.rename(columns={"spend_jan_sep_eur": "spend_eur"})
sp["campaign"] = sp.campaign.str.strip().replace("", "(none)")
assert set(sp.channel) <= set(df.channel)
assert set(sp.campaign) - {"(none)"} == set(df.campaign) - {"(none)"}
sp.groupby("channel", as_index=False).spend_eur.sum().to_csv(d / "spend_by_channel.csv", index=False)
sp[sp.campaign != "(none)"][["campaign", "channel", "spend_eur"]].to_csv(d / "spend_by_campaign.csv", index=False)
print("spend total", sp.spend_eur.sum())
