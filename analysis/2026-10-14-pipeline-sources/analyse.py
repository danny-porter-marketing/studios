import pandas as pd
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 30)
df = pd.read_csv("clean.csv")
sc = pd.read_csv("spend_by_channel.csv").set_index("channel").spend_eur
sp = pd.read_csv("spend_by_campaign.csv").set_index("campaign").spend_eur
def agg(g):
    t = df.groupby(g).agg(leads=("lead_id","count"), mql=("is_mql","sum"), sql=("is_sql","sum"), opp=("is_opp","sum"),
                          won=("is_won","sum"), pipeline=("pipeline_value_eur","sum"), rev=("won_value_eur","sum"))
    t["sql_rate"] = (t.sql/t.leads).round(3); t["mql_to_sql"] = (t.sql/t.mql).round(3)
    for c in ["leads","sql","pipeline","won","rev"]: t[c+"_sh"] = (t[c]/t[c].sum()).round(3)
    return t
tot = df[["is_mql","is_sql","is_opp","is_won","pipeline_value_eur","won_value_eur"]].sum()
print("TOTALS leads", len(df), tot.to_dict(), "spend", sc.sum())
print("pipe per eur", round(tot.pipeline_value_eur/sc.sum(),2), "cost/sql", round(sc.sum()/tot.is_sql,0))
c = agg("channel"); c["spend"]=sc; c["spend_sh"]=(c.spend/c.spend.sum()).round(3)
c["cost_sql"]=(c.spend/c.sql).round(0); c["pipe_per_eur"]=(c.pipeline/c.spend).round(1); c["win_rate_opp"]=(c.won/c.opp).round(2)
print(c.sort_values("pipeline",ascending=False).T)
k = agg("campaign"); k=k.drop("(none)"); k["spend"]=sp; k["cost_sql"]=(k.spend/k.sql.replace(0,float('nan'))).round(0); k["pipe_per_eur"]=(k.pipeline/k.spend).round(2)
print(k.sort_values("pipeline",ascending=False).T)
print("LI_AI+GA_Outs spend", sp[["LI_AI_Delivery_Q2","GA_Outsourcing_Generic"]].sum(), "sqls", k.loc[["LI_AI_Delivery_Q2","GA_Outsourcing_Generic"],"sql"].sum(),
      "pipeline", k.loc[["LI_AI_Delivery_Q2","GA_Outsourcing_Generic"],"pipeline"].sum(), "share of paid spend", round(sp[["LI_AI_Delivery_Q2","GA_Outsourcing_Generic"]].sum()/sp.sum(),3))
a = agg("first_asset"); print(a.sort_values("pipeline",ascending=False)[["leads","mql","sql","won","pipeline","sql_rate","mql_to_sql","leads_sh","sql_sh","pipeline_sh"]])
df["atype"]=df.first_asset.str.split(":").str[0]
at=agg("atype"); print(at[["leads","mql","sql","pipeline","sql_rate","mql_to_sql","leads_sh","sql_sh","pipeline_sh"]])
j = agg("job_title"); print(j.sort_values("sql_rate",ascending=False)[["leads","mql","sql","pipeline","sql_rate","mql_to_sql","pipeline_sh"]])
df["buyer"]=df.job_title.isin(["CTO","VP Engineering"])
print(agg("buyer")[["leads","sql","pipeline","sql_rate","leads_sh","pipeline_sh"]])
m = agg("created_month"); print(m[["leads","sql","opp","won","pipeline","sql_rate"]])
# partner without partner: sensitivity
print("excl partner: pipe per eur", round((tot.pipeline_value_eur-c.loc["Partner Referral","pipeline"])/(sc.sum()-8000),2))
print(pd.crosstab(df.channel, df.atype, values=df.pipeline_value_eur, aggfunc="sum").fillna(0).astype(int))
print(pd.crosstab(df.channel, df.atype))
