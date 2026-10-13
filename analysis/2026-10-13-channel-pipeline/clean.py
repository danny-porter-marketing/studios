import pandas as pd

df = pd.read_csv("raw.csv", dtype=str, keep_default_na=False)
n0 = len(df)
df = df.drop_duplicates()
print(f"rows {n0} -> {len(df)} (dropped {n0 - len(df)} exact duplicates)")

CHANNEL = {
    "linkedin ads": "LinkedIn Ads", "linkedin": "LinkedIn Ads",
    "google ads": "Google Ads", "google ppc": "Google Ads",
    "organic search": "Organic Search", "organic": "Organic Search", "seo": "Organic Search",
    "outbound email": "Outbound Email", "outbound": "Outbound Email", "cold email": "Outbound Email",
    "events": "Events", "event": "Events", "conference": "Events",
    "partner referral": "Partner Referral", "partner": "Partner Referral", "referral": "Partner Referral",
}
df["channel"] = df.source.str.strip().str.lower().map(CHANNEL)
assert df.channel.notna().all(), df[df.channel.isna()].source.unique()

# Two date formats: ISO and DD/MM/YYYY (day part goes up to 31, month part never above 9).
iso = pd.to_datetime(df.created_date, format="%Y-%m-%d", errors="coerce")
dmy = pd.to_datetime(df.created_date, format="%d/%m/%Y", errors="coerce")
df["created_date"] = iso.fillna(dmy)
assert df.created_date.notna().all()
df["month"] = df.created_date.dt.strftime("%Y-%m")
df["created_date"] = df.created_date.dt.strftime("%Y-%m-%d")

df["campaign"] = df.campaign.replace("", "(none)")
df["region"] = df.region.replace("", "Unknown")

TITLES = {"cto": "CTO", "ceo": "CEO", "vp engineering": "VP Engineering",
          "engineering manager": "Engineering Manager", "head of product": "Head of Product",
          "procurement": "Procurement", "developer": "Developer", "marketing manager": "Marketing Manager"}
df["job_title"] = df.job_title.str.strip().str.lower().map(TITLES)
assert df.job_title.notna().all()

text_money = df.deal_value_eur.str.contains("€").sum()
df["deal_value_eur"] = pd.to_numeric(df.deal_value_eur.str.replace("[€,]", "", regex=True), errors="coerce").fillna(0)
print(f"deal values stored as text converted: {text_money}")

RANK = {"Lead": 0, "MQL": 1, "SQL": 2, "Opportunity": 3, "Closed Won": 4, "Closed Lost": 4}
assert df.stage.isin(RANK).all()
r = df.stage.map(RANK)
df["is_mql"] = (r >= 1).astype(int)
df["is_sql"] = (r >= 2).astype(int)
df["is_opp"] = (r >= 3).astype(int)
df["is_won"] = (df.stage == "Closed Won").astype(int)
df["is_lost"] = (df.stage == "Closed Lost").astype(int)
df["pipeline_eur"] = df.deal_value_eur * df.is_opp
df["won_value_eur"] = df.deal_value_eur * df.is_won
assert (df[df.is_opp == 1].deal_value_eur > 0).all()

cols = ["lead_id", "created_date", "month", "channel", "source", "campaign", "first_asset", "job_title",
        "company_size", "region", "stage", "is_mql", "is_sql", "is_opp", "is_won", "is_lost",
        "deal_value_eur", "pipeline_eur", "won_value_eur"]
df[cols].to_csv("clean.csv", index=False)

sp = pd.read_csv("raw_spend.csv", keep_default_na=False)
ch = sp.groupby("channel", as_index=False).spend_jan_sep_eur.sum().rename(columns={"spend_jan_sep_eur": "spend_eur"})
assert set(ch.channel) == set(df.channel), (set(ch.channel) ^ set(df.channel))
ch.to_csv("spend_by_channel.csv", index=False)
cp = sp[sp.campaign != ""][["campaign", "channel", "spend_jan_sep_eur"]].rename(columns={"spend_jan_sep_eur": "spend_eur"})
assert set(cp.campaign) == set(df.campaign) - {"(none)"}
cp.to_csv("spend_by_campaign.csv", index=False)
print("clean rows", len(df))
