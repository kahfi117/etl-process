import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from etl.extract import extract_json, extract_csv
from etl.transform import transform_data
from etl.load import load_data

def run_etl(source="json"):
    print(f"📥 Extracting data from {source.upper()}...")

    if source == "json":
        df = extract_json()
    elif source == "csv":
        df = extract_csv()
    else:
        raise ValueError("Sumber data tidak valid! Gunakan 'json' atau 'csv'.")

    
    print("🔄 Transforming data...")
    dim_date, dim_provider, dim_location, dim_staff, dim_bed_capacity, fact_covid_cases = transform_data(df)

    print("📤 Loading data...")
    load_data(dim_date, dim_provider, dim_location, dim_staff, dim_bed_capacity, fact_covid_cases)

    print("✅ ETL process completed successfully!")

if __name__ == "__main__":
    run_etl()
