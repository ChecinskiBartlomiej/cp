#https://leetcode.com/problems/biggest-single-number/description/

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts=my_numbers.groupby("num").size()
    singles=counts.loc[counts==1]
    out=pd.DataFrame({"num": [singles.index.max()]})
    return out