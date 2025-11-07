# pylint: disable=(missing-module-docstring)
import io
import ast
import duckdb
import pandas as pd
import streamlit as st
from datetime import datetime as dt

con = duckdb.connect(database="data/exercices_table_sql.duckdb", read_only=False)


# solution_df = duckdb.sql(ANSWER).df()
st.header("enter your code")

with st.sidebar:
    theme = st.selectbox(
        "What would you like to work ? ",
        ["cross_joins", "GroupBy", "window_functions"],
        None,
        placeholder="Select something",
    )
    exercise = con.execute(f"SELECT * FROM memory_state WHERE Theme='{theme}'").df().sort_values(by = "last_reviewed").reset_index().drop(columns = 'index')
    # exercise["last_reviewed"] = pd.to_datetime(exercise['last_reviewed'])

    #print(exercise.loc[exercise["last_reviewed"] == exercise["last_reviewed"].min(), "exercice_name"].values)
    # Récupération de la solution de l'exercice
    try:
        st.dataframe(exercise)
        exercise_name = exercise.loc[exercise["last_reviewed"] == exercise["last_reviewed"].min(), "exercice_name"].values[0]
        with open(f"answer/{exercise_name}.sql") as f:
            answer = f.read()
        solution_df = con.execute(answer).df()

    except KeyError:
        st.write("Veuillez choisir le thème que vous voulez travailler")
    

query = st.text_area(
    label="Write your sql request (cross joins between 2 tables)", key="user_input"
)
if query:
    result = con.execute(query).df()
    st.write("Ton résultat")
    st.dataframe(result)

    # Comparaison du nombres de lignes et de colonnes dans le résultat
    ncol_missing = result.shape[1] - solution_df.shape[1]
    nrows_missing = result.shape[0] - solution_df.shape[0]

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError:
        st.write(
            "Impossible de comparer ton résultat avec la solution_df "
            "car les colonnes n'ont pas le même nom"
        )


tab1, tab2 = st.tabs(["Tables", "Solutions"])

with tab1:
    exercise_tables = exercise.loc[0, "tables"]
    for table in exercise_tables:
        st.write(f'Table: {table}')
        st.dataframe(con.execute(f"SELECT * FROM '{table}'").df())

with tab2:
    st.write(answer)
