from dagster import op

@op
def scrape_telegram_data():
    # Your scraping code here
    print("Scraping done")

@op
def load_raw_to_postgres():
    # Your PostgreSQL loading logic
    print("Data loaded")

@op
def run_dbt_transformations():
    # DBT transformation script
    print("DBT done")

@op
def run_yolo_enrichment():
    # Optional - maybe for ML model enrichment
    print("YOLO enrichment done")
