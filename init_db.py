import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercices_table_sql.duckdb", read_only= False)

# ---------------------
# Listes d'exercices
# --------------------
data = {
    'theme': ['cross_joins', 'cross_joins', 'window_functions'],
    'exercice_name': ['food_and_beverages', 'size_and_trademark', 'simple_window'],
    'tables': [['beverages', 'food_item'], ['size', 'trademark'], ['window_table']],
    'last_reviewed': ['2025-01-01', '1970-01-01', '1970-01-01'],
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE OR REPLACE TABLE memory_state AS SELECT * FROM memory_state_df")

# ----------------------
# CROSS JOIN EXERCICES
# ----------------------

# Food and beverages

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

# Taille de t-shirt et marque de commerce
size = """
size
XS
S
M
L
XL
"""
size = pd.read_csv(io.StringIO(size))
con.execute("CREATE OR REPLACE TABLE size AS SELECT * FROM size")

trademark = """
trademark
Nike
Addidas
Puma
Coq_Sportif
Lewis
"""
trademark = pd.read_csv(io.StringIO(trademark))
con.execute("CREATE OR REPLACE TABLE trademark AS SELECT * FROM trademark")
