#https://leetcode.com/problems/not-boring-movies/description/

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[(cinema["id"]%2==1) & (cinema["description"]!="boring")].sort_values(by=["rating"],ascending=False)