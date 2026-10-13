import pandas as pd, sys
d = sys.argv[1]
df = pd.read_csv(f"{d}/clean.csv"); sc = pd.read_csv(f"{d}/spend_by_channel.csv"); sp = pd.read_csv(f"{d}/spend_by_campaign.csv")
m = ["is_mql","is_sql","is_opp","is_won","pipeline_value_eur","won_value_eur"]
tot = df[m].sum(); tot["leads"] = len(df); tot["spend"] = sc.spend_eur.sum()
tot["cost_per_sql"] = tot.spend / tot.is_sql; tot["lead_to_sql"] = tot.is_sql / tot.leads
tot["pipeline_per_eur"] = tot.pipeline_value_eur / tot.spend
print(tot.round(4).to_string())
def br(col, spend=None):
    g = df.groupby(col).agg(leads=("lead_id","count"), **{k:(k,"sum") for k in m})
    g["sql_rate"] = (g.is_sql/g.leads).round(4)
    g["sql_share"] = (g.is_sql/tot.is_sql).round(4); g["lead_share"] = (g.leads/tot.leads).round(4)
    if spend is not None:
        g = g.join(spend.set_index(col).spend_eur)
        g["cost_per_lead"] = (g.spend_eur/g.leads).round(0); g["cost_per_sql"] = (g.spend_eur/g.is_sql).round(0)
        g["pipeline_per_eur"] = (g.pipeline_value_eur/g.spend_eur).round(2)
    print(f"\n### {col}\n", g.sort_values("leads", ascending=False).to_string())
br("channel", sc); br("campaign", sp[["campaign","spend_eur"]]); br("first_asset"); br("job_title")
cs = df.first_asset.str.startswith("Case study")
print("\ncase study sql rate", df[cs].is_sql.mean().round(4), "other", df[~cs].is_sql.mean().round(4))
print(pd.crosstab(df.month, df.stage))
