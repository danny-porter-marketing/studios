"""raw.csv + raw_spend.csv -> clean.csv, spend_by_channel.csv, spend_by_campaign.csv. Every fix is explicit."""
import pandas as pd

GBP_TO_EUR = 1.17  # ASSUMPTION: no rate supplied. Applies to 7 deals only. Replace with finance's rate.

SOURCE_TO_CHANNEL = {
    "Google": "Paid Search", "PPC": "Paid Search", "Paid Search": "Paid Search",
    "Meta": "Paid Social", "Facebook Ads": "Paid Social", "linkedin paid": "Paid Social", "Paid Social": "Paid Social",
    "Organic": "Content / SEO", "seo": "Content / SEO", "Content / SEO": "Content / SEO",
    "SDR": "SDR Outbound", "Outbound": "SDR Outbound", "SDR Outbound": "SDR Outbound",
    "Webinar": "Webinars", "Webinars": "Webinars", "Online event": "Webinars",
    "Referral": "Referral", "Client referral": "Referral",
    "Partner": "Partner",
}
PLATFORM = {"Meta": "Meta", "Facebook Ads": "Meta", "linkedin paid": "LinkedIn", "Paid Social": "Not recorded"}
STAGE_ORDER = {"New": 0, "Marketing Qualified": 1, "Sales Qualified": 2, "Proposal": 3, "Won": 4, "Lost": 3}
log = []

df = pd.read_csv("raw.csv", dtype=str, keep_default_na=False)
n0 = len(df)

n = len(df); df = df.drop_duplicates(); log.append(f"Removed {n - len(df)} exact duplicate rows")
m = df["Record ID"].eq("TOTAL"); log.append(f"Removed {m.sum()} TOTAL row (contained '=SUM()')"); df = df[~m]
m = df["Company"].str.contains("Corvane", case=False); log.append(
    f"Removed {m.sum()} internal test rows (IDs Q0 to Q4, 'Corvane (internal)', Won at 120000 each)"); df = df[~m]

iso = pd.to_datetime(df["Create Date"], format="%Y-%m-%d", errors="coerce")
us = pd.to_datetime(df["Create Date"], format="%m/%d/%Y", errors="coerce")
log.append(f"Parsed {iso.isna().sum()} MM/DD/YYYY dates to ISO (first part never exceeds 12, second reaches 31)")
df["create_date"] = iso.fillna(us)
assert df["create_date"].notna().all()
m = df["create_date"] >= "2026-09-01"
log.append(f"Excluded {m.sum()} leads created in September: outside the Jan to Aug spend window"); df = df[~m]
df["month"] = df["create_date"].dt.strftime("%Y-%m")

df["channel"] = df["Original Source"].map(SOURCE_TO_CHANNEL)
assert df["channel"].notna().all(), df.loc[df["channel"].isna(), "Original Source"].unique()
df["paid_social_platform"] = df["Original Source"].map(PLATFORM).fillna("")
df["campaign"] = df["Campaign"].replace("", "(none)")
df["first_asset"] = df["First Conversion"]
df["job_title"] = df["Job Title"].str.strip().str.title().str.replace(" Of ", " of ").replace({"Cto": "CTO", "Vp of Engineering": "VP of Engineering"})
df["country"] = df["Country"].replace("", "Unknown")
df["stage"] = df["Lifecycle Stage"]
assert df["stage"].isin(STAGE_ORDER).all()

amt = df["Deal Amount"]
gbp = amt.str.startswith("£")
log.append(f"Converted {gbp.sum()} GBP text amounts (e.g. '£53,800') to EUR at an assumed {GBP_TO_EUR}")
num = pd.to_numeric(amt.str.replace(r"[£€,]", "", regex=True), errors="coerce")
df["deal_eur"] = (num * gbp.map({True: GBP_TO_EUR, False: 1.0})).round(0).fillna(0)

rank = df["stage"].map(STAGE_ORDER)
df["is_mql"] = (rank >= 1).astype(int)
df["is_sql"] = (rank >= 2).astype(int)
df["is_opp"] = df["stage"].isin(["Proposal", "Won", "Lost"]).astype(int)
df["is_won"] = (df["stage"] == "Won").astype(int)
df["pipeline_eur"] = df["deal_eur"] * df["is_opp"]
df["won_value_eur"] = df["deal_eur"] * df["is_won"]
assert (df.loc[df.is_opp == 1, "deal_eur"] > 0).all() and (df.loc[df.is_opp == 0, "deal_eur"] == 0).all()

cols = ["Record ID", "create_date", "month", "channel", "paid_social_platform", "Original Source", "campaign",
        "first_asset", "job_title", "country", "Company", "stage", "is_mql", "is_sql", "is_opp", "is_won",
        "deal_eur", "pipeline_eur", "won_value_eur"]
df["create_date"] = df["create_date"].dt.strftime("%Y-%m-%d")
df[cols].rename(columns={"Record ID": "record_id", "Original Source": "source_raw", "Company": "company"}).to_csv("clean.csv", index=False)
log.append(f"Leads: {n0} raw rows -> {len(df)} clean rows")

sp = pd.read_csv("raw_spend.csv", dtype={"campaign": str}, keep_default_na=False)
dup = sp.duplicated(["month", "channel", "campaign"], keep="first")
log.append(f"Spend: dropped {dup.sum()} conflicting duplicate row (2026-08 PPC_Dedicated_Team at 3150; kept 3005)")
sp = sp[~dup]
assert set(sp["channel"]) <= set(SOURCE_TO_CHANNEL.values())
sp.groupby("channel", as_index=False)["spend_eur"].sum().to_csv("spend_by_channel.csv", index=False)
sp[sp.campaign != ""].groupby("campaign", as_index=False)["spend_eur"].sum().to_csv("spend_by_campaign.csv", index=False)
sp.to_csv("spend_monthly_clean.csv", index=False)
print("\n".join(log))
