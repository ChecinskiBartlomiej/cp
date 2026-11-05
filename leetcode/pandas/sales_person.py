#https://leetcode.com/problems/sales-person/description/

import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders_company=orders.merge(company,on="com_id",how="left")
    red_sales=orders_company.loc[orders_company["name"]=="RED","sales_id"]
    return sales_person.loc[~sales_person["sales_id"].isin(red_sales),["name"]]