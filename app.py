import streamlit as st
from router import route_query

st.title("🛍️ Customer Support AI Agent")

user_query = st.text_input("Ask your question")

if st.button("Submit"):
    answer = route_query(user_query)
    st.write(answer)