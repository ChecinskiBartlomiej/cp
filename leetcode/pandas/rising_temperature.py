#https://leetcode.com/problems/rising-temperature/

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values("recordDate")
    previous_temp = weather["temperature"].shift(1)
    previous_date = weather["recordDate"].shift(1)
    condition = (
        (weather["temperature"] > previous_temp) &
        ((weather["recordDate"] - previous_date).dt.days == 1)
    )
    return weather.loc[condition, ["id"]]