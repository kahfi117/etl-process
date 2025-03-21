import duckdb
from config.settings import DUCKDB_PATH

def load_data(dim_date, dim_provider, dim_location, dim_staff, dim_bed_capacity, fact_covid_cases):
    conn = duckdb.connect(DUCKDB_PATH)

    dim_date.to_sql("dim_date", conn, if_exists="replace", index=False)
    dim_provider.to_sql("dim_provider", conn, if_exists="replace", index=False)
    dim_location.to_sql("dim_location", conn, if_exists="replace", index=False)
    dim_staff.to_sql("dim_staff", conn, if_exists="replace", index=False)
    dim_bed_capacity.to_sql("dim_bed_capacity", conn, if_exists="replace", index=False)
    fact_covid_cases.to_sql("fact_covid_cases", conn, if_exists="replace", index=False)

    conn.close()
