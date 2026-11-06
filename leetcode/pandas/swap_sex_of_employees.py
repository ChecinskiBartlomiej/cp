#https://leetcode.com/problems/swap-sex-of-employees/description/

import pandas as pd

def swap_salary(salary: pd.DataFrame) -> None:
    salary["sex"]=salary["sex"].replace({
        "m": "f",
        "f": "m"
    })
    return salary