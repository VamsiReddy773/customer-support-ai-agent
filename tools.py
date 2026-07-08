import pandas as pd

orders = pd.read_csv("sample_data/orders.csv")


def get_order_details(order_id):
    result = orders[orders["order_id"] == order_id]

    if result.empty:
        return "Order not found."

    return result.to_dict(orient="records")[0]


def order_lookup(order_id):
    return get_order_details(order_id)