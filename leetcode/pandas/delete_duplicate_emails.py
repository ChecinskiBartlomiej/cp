#https://leetcode.com/problems/delete-duplicate-emails/description/

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values("id", inplace=True)
    duplicates=person.duplicated(subset="email")
    person.drop(index=person[duplicates].index, inplace=True)