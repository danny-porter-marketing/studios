import pandas as pd
pd.set_option("display.width", 200); pd.set_option("display.max_columns", 20)
df = pd.read_csv("clean.csv"); sc = pd.read_csv("spend_by_channel.csv"); sp = pd.read_csv("spend_by_campaign.csv")
agg = dict(leads=("lead_id","count"), mql=("is_mql","sum"), sql=("is_sql","sum"), opp=("is_opp","sum"),
           won=("is_won","sum"), pipeline=("pipeline_value_eur","sum"), wonv=("won_value_eur","sum"))
print("TOTAL", {k: df[c].sum() if f=="sum" else len(df) for k,(c,f) in agg.items()}, "spend", sc.spend_eur.sum())
def show(g, spend=None, key=None):
    t = df.groupby(g).agg(**agg)
    if spend is not None: t = t.join(spend.set_index(key).spend_eur)
    t["sql_rate"] = (t.sql/t.leads).round(3)
    if spend is not None:
        t["cost_per_sql"] = (t.spend_eur/t.sql).round(0); t["pipe_per_eur"] = (t.pipeline/t.spend_eur).round(2)
    print(t.sort_values("pipeline", ascending=False), "\n")
show("channel", sc, "channel"); show("campaign", sp, "campaign"); show("first_asset"); show("job_title")
print(df.groupby("created_month").agg(**agg))
print(pd.crosstab(df.first_asset, df.channel, values=df.is_sql, aggfunc="sum"))
