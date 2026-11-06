#https://leetcode.com/problems/reformat-department-table/description/

import pandas as pd

data={
    "id": [1,2,3,1,1],
    "revenue": [8000,9000,10000,7000,6000],
    "month": ["Jan","Jan","Feb","Feb","Mar"]
}
df=pd.DataFrame(data)

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    out=department.pivot(
        index="id",
        columns="month",
        values="revenue"
    )
    out=out.reindex(columns=months)
    out.columns=[month+"_Revenue" for month in months]
    out=out.reset_index()
    return out
