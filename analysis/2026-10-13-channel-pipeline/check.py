import pandas as pd
d = pd.read_csv("clean.csv"); ch = pd.read_csv("spend_by_channel.csv"); cp = pd.read_csv("spend_by_campaign.csv")
agg = dict(leads=("lead_id","count"), mqls=("is_mql","sum"), sqls=("is_sql","sum"), opps=("is_opp","sum"),
           won=("is_won","sum"), pipeline=("pipeline_eur","sum"), won_eur=("won_value_eur","sum"))
tot = d.agg({"lead_id":"count","is_mql":"sum","is_sql":"sum","is_opp":"sum","is_won":"sum","pipeline_eur":"sum","won_value_eur":"sum"})
print(tot.to_string()); print("spend", ch.spend_eur.sum(), "cost/SQL", round(ch.spend_eur.sum()/tot.is_sql), "pipe/spend", round(tot.pipeline_eur/ch.spend_eur.sum(),2))
for g, sp, key in [("channel", ch, "channel"), ("campaign", cp, "campaign"), ("first_asset", None, None), ("job_title", None, None)]:
    t = d.groupby(g).agg(**agg)
    if sp is not None:
        t = t.join(sp.set_index(key).spend_eur)
        t["cost_per_sql"] = (t.spend_eur / t.sqls).round(0)
        t["pipe_per_eur"] = (t.pipeline / t.spend_eur).round(2)
    t["sql_rate"] = (t.sqls / t.leads * 100).round(1)
    t["opp_rate"] = (t.opps / t.leads * 100).round(1)
    t["sql_share"] = (t.sqls / tot.is_sql * 100).round(1)
    t["pipe_share"] = (t.pipeline / tot.pipeline_eur * 100).round(1)
    t["lead_share"] = (t.leads / tot.lead_id * 100).round(1)
    print("\n", t.sort_values("pipeline", ascending=False).to_string())
print("\n", pd.crosstab(d.first_asset, d.channel, values=d.is_sql, aggfunc="sum").to_string())
print("\nby month:", d.groupby("month").agg(**agg).to_string())
