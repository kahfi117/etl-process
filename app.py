import duckdb

conn = duckdb.connect("data/database/test_warehouse.db")  

data = conn.execute("SELECT count(*) FROM fact_covid_cases").fetchall()

print("Users in database:", data)

conn.close()