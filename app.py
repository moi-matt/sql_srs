import streamlit as st
import pandas as pd
import duckdb
import io
st.write("Hello world")

csv = """
Beverage, prive
orange juice, 2.5
Espresso, 3
Latte machiatto, 10
tea, 5
"""
beverages = pd.read_csv(io.StringIO(csv))

csv2 = """
food_item, food_price
cookie, 2.5
donut, 4
muffin, 5  
"""
food_item = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT *
FROM beverages
CROSS JOIN food_item
"""
solution = duckdb.sql(answer).df()
st.header("enter your code")

with st.sidebar:
    option = st.selectbox(
        "What would you like to work ? ",
        [
            "Basic select",
            "Basic Joins",
            "Window function"
        ],
        0,
        placeholder="Select something"
    )
    st.write('You chose to work on', option)

query = st.text_area(label="Write your sql request", key="user_input")
if query:
    result = duckdb.sql(query).df()
    st.write("Ton résultat")
    st.dataframe(result)
tab1, tab2 = st.tabs(["tables", "solution"])

with tab1:
    st.write("Table : boissons")
    st.dataframe(beverages)
    st.write("Table : aliments")
    st.dataframe(food_item)
    st.write("Expected :")
    st.dataframe(solution)

with tab2:
    st.write(answer)


