#https://leetcode.com/problems/classes-with-at-least-5-students/description/

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    classes=courses.groupby("class").size()
    result=classes[classes>=5]
    return pd.DataFrame({"class": result.index})