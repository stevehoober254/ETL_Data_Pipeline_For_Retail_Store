from airflow import DAG

# DAG configuration
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),  # Start date for the DAG
    'schedule_interval': None,  # Set a schedule interval (e.g., '@daily') for periodic execution
}

with DAG(
        dag_id='etl_pipeline',
        default_args=default_args,
        catchup=False  # Set catchup=True for backfilling data for past dates (optional)
) as dag:

    # Define a PythonOperator task to run the ETL script
    run_etl_task = PythonOperator(
        task_id='run_etl',
        python_callable=run_etl,
        provide_context=True  # Optionally pass context to the ETL script
    )