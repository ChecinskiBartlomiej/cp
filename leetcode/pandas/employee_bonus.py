#https://leetcode.com/problems/employee-bonus/description/

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged=employee.merge(bonus,on="empId",how="left")
    result=merged[(merged["bonus"]<1000) | (merged["bonus"].isna())].loc[:,["name","bonus"]]
    return result