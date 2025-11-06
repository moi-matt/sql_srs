import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercices_table_sql.duckdb", read_only= False)

# ---------------------
# Listes d'exercices
# --------------------
data = {
    'theme': ['cross_joins', 'window_functions'],
    'exercice_name': ['food_and_beverages', 'simple_window'],
    'tables': [['beverages', 'food_item'], 'window_table'],
    'last_reviewed': ['1970-01-01', '1970-01-01'],
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")

# ----------------------
# CROSS JOIN EXERCICES
# ----------------------

CSV = """
beverage,price
orange juice,2.5
Espresso,3
Latte machiatto,10
tea,5
"""
beverages = pd.read_csv(io.StringIO(CSV))

con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * from beverages")

CSV2 = """
food_item,food_price
cookie,2.5
donut,4
muffin,5  
"""
food_item = pd.read_csv(io.StringIO(CSV2))
con.execute("CREATE TABLE IF NOT EXISTS food_item AS SELECT * from food_item")
