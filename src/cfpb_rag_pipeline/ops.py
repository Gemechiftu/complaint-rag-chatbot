from dagster import op

@op
def scrape_telegram_data():
    print("Scraping telegram data...")

@op
def load_raw_to_postgres():
    print("Loading data to Postgres...")

@op
def run_dbt_transformations():
    print("Running DBT transformations...")

@op
def run_yolo_enrichment():
    print("Running YOLO enrichment...")
