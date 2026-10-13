"""raw.csv + raw_spend.csv -> clean.csv, spend_by_channel.csv, spend_by_campaign.csv"""
import pandas as pd

CHANNEL_MAP = {
    "linkedin ads": "LinkedIn Ads", "LinkedIn": "LinkedIn Ads", "LinkedIn Ads": "LinkedIn Ads",
    "google ads": "Google Ads", "Google PPC": "Google Ads", "Google Ads": "Google Ads",
    "Organic Search": "Organic Search", "SEO": "Organic Search", "organic": "Organic Search",
    "outbound": "Outbound Email", "Outbound Email": "Outbound Email", "Cold Email": "Outbound Email",
    "Event": "Events", "Conference": "Events", "Events": "Events",
    "partner": "Partner Referral", "Partner Referral": "Partner Referral", "Referral": "Partner Referral",
}
TITLE_FIX = {t.lower(): t for t in ["CTO", "CEO", "VP Engineering", "Engineering Manager", "Developer",
                                    "Head of Product", "Marketing Manager", "Procurement"]}
SQL_PLUS = {"SQL", "Opportunity", "Closed Won", "Closed Lost"}
OPP_PLUS = {"Opportunity", "Closed Won", "Closed Lost"}

raw = pd.read_csv("raw.csv", dtype=str, keep_default_na=False)
df = raw.drop_duplicates()
print(f"rows {len(raw)} -> {len(df)} (dropped {len(raw) - len(df)} exact duplicates)")
assert df.lead_id.is_unique

df["channel"] = df.source.map(CHANNEL_MAP)
assert df.channel.notna().all(), df.source[df.channel.isna()].unique()
df["campaign"] = df.campaign.replace("", "(none)")
iso = pd.to_datetime(df.created_date, format="%Y-%m-%d", errors="coerce")
dmy = pd.to_datetime(df.created_date, format="%d/%m/%Y", errors="coerce")
df["created_date"] = iso.fillna(dmy)
assert df.created_date.notna().all()
print("DD/MM dates converted:", (iso.isna()).sum())
df["created_month"] = df.created_date.dt.strftime("%Y-%m")
df["created_date"] = df.created_date.dt.strftime("%Y-%m-%d")
df["job_title"] = df.job_title.str.strip().str.lower().map(TITLE_FIX)
assert df.job_title.notna().all()
df["region"] = df.region.replace("", "Unknown")
txt = df.deal_value_eur.str.contains("€")
print("deal values stored as text:", txt.sum())
df["deal_value_eur"] = pd.to_numeric(df.deal_value_eur.str.replace(r"[€,]", "", regex=True), errors="coerce").fillna(0)

df["is_mql"] = (df.stage != "Lead").astype(int)
df["is_sql"] = df.stage.isin(SQL_PLUS).astype(int)
df["is_opp"] = df.stage.isin(OPP_PLUS).astype(int)
df["is_won"] = (df.stage == "Closed Won").astype(int)
df["pipeline_value_eur"] = df.deal_value_eur * df.is_opp
df["won_value_eur"] = df.deal_value_eur * df.is_won
assert (df.deal_value_eur > 0).eq(df.is_opp == 1).all(), "deal value present outside opportunities"

cols = ["lead_id", "created_date", "created_month", "channel", "source", "campaign", "first_asset", "job_title",
        "company_size", "region", "stage", "is_mql", "is_sql", "is_opp", "is_won",
        "pipeline_value_eur", "won_value_eur"]
df = df.sort_values(["created_date", "lead_id"])
df[cols].to_csv("clean.csv", index=False)

sp = pd.read_csv("raw_spend.csv", keep_default_na=False)
sp = sp.rename(columns={"spend_jan_sep_eur": "spend_eur"})
assert set(sp.channel) == set(df.channel), (set(sp.channel), set(df.channel))
sp.groupby("channel", as_index=False).spend_eur.sum().to_csv("spend_by_channel.csv", index=False)
spc = sp[sp.campaign != ""][["campaign", "channel", "spend_eur"]]
assert set(spc.campaign) == set(df.campaign) - {"(none)"}
spc.to_csv("spend_by_campaign.csv", index=False)
print("channel x campaign check:\n", pd.crosstab(df.campaign, df.channel))
