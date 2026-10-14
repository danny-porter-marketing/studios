"""raw.csv + raw_spend.csv -> clean.csv, spend_by_channel.csv, spend_by_campaign.csv. Every fix is explicit."""
import pandas as pd

df = pd.read_csv("raw.csv", dtype=str, keep_default_na=False)
n0 = len(df)
log = {}

# 1. Exact duplicates only. Lead IDs are unique afterwards.
log["exact_dups_removed"] = int(df.duplicated().sum())
df = df.drop_duplicates().reset_index(drop=True)
assert df.lead_id.is_unique

# 2. Source spellings -> channel names that match the spend file
CHANNEL = {
    "linkedin ads": "LinkedIn Ads", "LinkedIn": "LinkedIn Ads", "LinkedIn Ads": "LinkedIn Ads",
    "google ads": "Google Ads", "Google PPC": "Google Ads", "Google Ads": "Google Ads",
    "Organic Search": "Organic Search", "SEO": "Organic Search", "organic": "Organic Search",
    "outbound": "Outbound Email", "Outbound Email": "Outbound Email", "Cold Email": "Outbound Email",
    "Event": "Events", "Conference": "Events", "Events": "Events",
    "partner": "Partner Referral", "Partner Referral": "Partner Referral", "Referral": "Partner Referral",
}
unmapped = set(df.source) - set(CHANNEL)
assert not unmapped, unmapped
df.insert(2, "channel", df.source.map(CHANNEL))
log["source_rows_renamed"] = int((df.source != df.channel).sum())

# 3. Dates: ISO stays, DD/MM/YYYY converted (verified: first part >12 in 121 rows, second part never >12)
slash = df.created_date.str.contains("/")
log["dates_converted"] = int(slash.sum())
d = pd.to_datetime(df.created_date.where(~slash), format="%Y-%m-%d", errors="coerce")
d = d.fillna(pd.to_datetime(df.created_date.where(slash), format="%d/%m/%Y", errors="coerce"))
assert d.notna().all()
df["created_date"] = d.dt.strftime("%Y-%m-%d")
df.insert(2, "created_month", d.dt.strftime("%Y-%m"))

# 4. Deal values stored as text ('€61,700') -> numbers
txt = df.deal_value_eur.str.contains(r"[€,]")
log["deal_values_text_fixed"] = int(txt.sum())
dv = pd.to_numeric(df.deal_value_eur.str.replace(r"[€,\s]", "", regex=True).replace("", None), errors="coerce")
assert dv.notna().sum() == (df.deal_value_eur != "").sum()

# 5. Grouping columns: casing, blanks
TITLE_CASE = {"cto": "CTO", "ceo": "CEO", "vp engineering": "VP Engineering",
              "engineering manager": "Engineering Manager", "developer": "Developer",
              "procurement": "Procurement", "marketing manager": "Marketing Manager",
              "head of product": "Head of Product"}
fixed = df.job_title.map(TITLE_CASE).fillna(df.job_title)
log["job_titles_recased"] = int((fixed != df.job_title).sum())
df["job_title"] = fixed
log["blank_regions"] = int((df.region == "").sum())
df["region"] = df.region.replace("", "Unknown")
log["blank_campaigns"] = int((df.campaign == "").sum())
df["campaign"] = df.campaign.replace("", "(none)")

# 6. Cumulative stage flags
STAGES = ["Lead", "MQL", "SQL", "Opportunity", "Closed Won", "Closed Lost"]
assert set(df.stage) <= set(STAGES)
df["is_mql"] = (df.stage != "Lead").astype(int)
df["is_sql"] = df.stage.isin(["SQL", "Opportunity", "Closed Won", "Closed Lost"]).astype(int)
df["is_opp"] = df.stage.isin(["Opportunity", "Closed Won", "Closed Lost"]).astype(int)
df["is_won"] = (df.stage == "Closed Won").astype(int)
assert (dv.notna() == (df.is_opp == 1)).all()  # deal value exists exactly on opportunities
df["pipeline_value_eur"] = (dv.fillna(0) * df.is_opp).round(0).astype(int)
df["won_value_eur"] = (dv.fillna(0) * df.is_won).round(0).astype(int)
df = df.drop(columns=["deal_value_eur"])
df = df.sort_values(["created_date", "lead_id"])
df.to_csv("clean.csv", index=False)

# Spend lookup tables
sp = pd.read_csv("raw_spend.csv")
sp["channel"] = sp.channel.str.strip()
assert set(sp.channel) == set(df.channel), (set(sp.channel) ^ set(df.channel))
sp.groupby("channel", as_index=False).spend_jan_sep_eur.sum().rename(columns={"spend_jan_sep_eur": "spend_eur"}).to_csv("spend_by_channel.csv", index=False)
camp = sp.dropna(subset=["campaign"])[["campaign", "channel", "spend_jan_sep_eur"]].rename(columns={"spend_jan_sep_eur": "spend_eur"})
assert set(camp.campaign) == set(df.campaign) - {"(none)"}
camp.to_csv("spend_by_campaign.csv", index=False)

print("rows", n0, "->", len(df)); print(log)
