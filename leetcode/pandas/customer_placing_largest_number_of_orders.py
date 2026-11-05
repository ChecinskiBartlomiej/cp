#https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    counts=orders.groupby("customer_number").size()
    customer=counts.idxmax()
    return pd.DataFrame({"customer_number": [customer]})