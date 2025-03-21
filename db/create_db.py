import duckdb
import os
from config.settings import DUCKDB_PATH

def create_database():
    """Membuat database DuckDB berdasarkan schema.sql"""
    con = duckdb.connect(DUCKDB_PATH)

    with open("db/schema.sql", "r") as f:
        schema_sql = f.read()

    con.execute(schema_sql)
    con.close()

if __name__ == "__main__":
    create_database()
    print("Database DuckDB berhasil dibuat dengan tabel yang sesuai.")
