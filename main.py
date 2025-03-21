from etl.etl_pipeline import run_etl
import sys

if __name__ == "__main__":
    source_type = sys.argv[1] if len(sys.argv) > 1 else "json"
    run_etl(source_type)