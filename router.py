import re

from rag import get_retriever
from tools import order_lookup


def extract_order_id(query):
    match = re.search(r"ORD\d+", query.upper())

    if match:
        return match.group()

    return None


def route_query(query):
    order_id = extract_order_id(query)

    if order_id:
        return order_lookup(order_id)

    retriever = get_retriever()
    docs = retriever.invoke(query)

    if not docs:
        return "Sorry, I couldn't find any relevant information."

    return docs[0].page_content

