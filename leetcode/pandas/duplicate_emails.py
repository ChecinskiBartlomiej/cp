#https://leetcode.com/problems/duplicate-emails/description/

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    result = person[person.duplicated(subset=["email"])]
    return result[["email"]].drop_duplicates().rename(
        columns={"email": "Email"}
    )
