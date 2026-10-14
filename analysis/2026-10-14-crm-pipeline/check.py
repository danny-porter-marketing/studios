import pandas as pd
d=pd.read_csv("clean.csv"); sc=pd.read_csv("spend_by_channel.csv"); sp=pd.read_csv("spend_by_campaign.csv")
print(d.job_title.value_counts().to_dict())
k=dict(leads=len(d),mql=d.is_mql.sum(),sql=d.is_sql.sum(),opp=d.is_opp.sum(),won=d.is_won.sum(),
 pipeline=d.pipeline_eur.sum(),won_eur=d.won_value_eur.sum(),spend=sc.spend_eur.sum())
k["cost_per_sql"]=k["spend"]/k["sql"]; k["lead_to_sql"]=k["sql"]/k["leads"]; print(k)
def tab(g,spend=None,key=None):
    t=d.groupby(g).agg(leads=("record_id","size"),sql=("is_sql","sum"),opp=("is_opp","sum"),won=("is_won","sum"),pipeln=("pipeline_eur","sum"),won_eur=("won_value_eur","sum"))
    t["sql_rate"]=(t.sql/t.leads).round(3)
    if spend is not None:
        t=t.join(spend.set_index(key)); t["cpsql"]=(t.spend_eur/t.sql).round(0); t["pipe_per_eur"]=(t.pipeln/t.spend_eur).round(2)
    print(t.sort_values("pipeln",ascending=False).to_string(),"\n")
tab("channel",sc,"channel"); tab("campaign",sp,"campaign"); tab("first_asset"); tab("job_title"); tab("paid_social_platform")
# share of SQL / pipeline
t=d.groupby("channel")[["record_id"]].size(); print((d.groupby("channel").is_sql.sum()/d.is_sql.sum()).round(3).to_dict()); print((t/len(d)).round(3).to_dict())
print((d.groupby("channel").pipeline_eur.sum()/d.pipeline_eur.sum()).round(3).to_dict())
# buyer vs non-buyer titles
d["buyer"]=~d.job_title.isin(["Recruiter","Student","Software Engineer"])
print(d.groupby(["campaign","buyer"]).size().unstack().assign(share=lambda x:(x[False]/(x[False]+x[True])).round(3)))
# month cohort: SQL rate by month
print(d.groupby("month").agg(leads=("record_id","size"),sql=("is_sql","sum"),opp=("is_opp","sum")).assign(r=lambda x:(x.sql/x.leads).round(3)))
