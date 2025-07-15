from dagster import job
from ..ops.my_ops import scrape_telegram_data, load_raw_to_postgres, run_dbt_transformations, run_yolo_enrichment

@job
def rag_pipeline_job():
    data = scrape_telegram_data()
    loaded = load_raw_to_postgres()
    run_dbt_transformations()
    run_yolo_enrichment()
