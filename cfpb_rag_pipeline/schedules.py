from dagster import schedule
from .jobs import full_pipeline_job

@schedule(cron_schedule="0 0 * * *", job=full_pipeline_job, execution_timezone="Africa/Addis_Ababa")
def daily_job_schedule(_context):
    return {}
