import streamlit as st
import pandas as pd
import duckdb as db

st.write("Hello world")

tab1, tab2 = st.tabs(["ma_table", "autre_table"])

option = st.selectbox(
    "What would you like to work ? ",
    ["Basic select",
     "Basic Joins",
     "Window function"],
     0,
)

st.write(f'You chose to work on {option}')


# df = pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]})
# # with tab1 :
# input_test = st.text_area(label="Entrez le texte")

# if input_test == "":
#     input_test = "SELECT * FROM df"

# st.dataframe(db.sql(input_test).df())

# with tab2 :
#     super_texte = st.text_area(label = "Entrez le texte")
#     st.write(super_texte)
