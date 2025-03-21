import os

API_URL = os.getenv("API_URL", "https://data.cms.gov/data-api/v1/dataset/137f90cb-ac53-4b3d-8358-e65cf64e03d3/data")
DUCKDB_PATH = os.getenv("DUCKDB_PATH", "data/database/test_warehouse.db")