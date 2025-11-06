# pylint: disable=(missing-module-docstring)
import io
import ast
import duckdb
import pandas as pd
import streamlit as st

con = duckdb.connect(database="data/exercices_table_sql.duckdb", read_only=False)


# solution_df = duckdb.sql(ANSWER).df()
st.header("enter your code")

with st.sidebar:
    theme = st.selectbox(
        "What would you like to work ? ",
        ["cross_joins", "GroupBy", "window_functions"],
        0,
        placeholder="Select something",
    )
    exercise = con.execute(f"SELECT * FROM memory_state WHERE Theme='{theme}'").df()
    st.write(exercise)

query = st.text_area(
    label="Write your sql request (cross joins between 2 tables)", key="user_input"
)
# if query:
#     result = duckdb.sql(query).df()
#     st.write("Ton résultat")
#     st.dataframe(result)

#     # Comparaison du nombres de lignes et de colonnes dans le résultat
#     ncol_missing = result.shape[1] - solution_df.shape[1]
#     nrows_missing = result.shape[0] - solution_df.shape[0]

#     try:
#         result = result[solution_df.columns]
#         st.dataframe(result.compare(solution_df))
#     except KeyError:
#         st.write(
#             "Impossible de comparer ton résultat avec la solution_df "
#             "car les colonnes n'ont pas le même nom"
#         )

# tab1, tab2 = st.tabs(["tables", "solution_df"])

# with tab1:
#     st.write("Table : boissons")
#     st.dataframe(beverages)
#     st.write("Table : aliments")
#     st.dataframe(food_item)
#     st.write("Expected :")
#     st.dataframe(solution_df)

with tab2:
    exercice_tables = ast.literal_eval(exercice.loc[0, "tables"])
    for table in exercice_tables:
        st.write(f'Table: {table}')
        st.dataframe()
