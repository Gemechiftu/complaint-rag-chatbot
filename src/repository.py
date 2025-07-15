from dagster import job, op

@op
def scrape_telegram_data():
    print("Scraping Telegram data...")

@op
def load_raw_to_postgres():
    print("Loading data to Postgres...")

@op
def run_dbt_transformations():
    print("Running DBT transformations...")

@op
def run_yolo_enrichment():
    print("Running YOLO enrichment...")

@job
def complaint_rag_pipeline():
    data = scrape_telegram_data()
    load = load_raw_to_postgres(start_after=data)
    transform = run_dbt_transformations(start_after=load)
    run_yolo_enrichment(start_after=transform)
