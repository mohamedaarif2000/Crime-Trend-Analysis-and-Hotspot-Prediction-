from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {'start_date': datetime(2024, 1, 1)}

with DAG('crime_analysis_pipeline', default_args=default_args, schedule_interval='@daily') as dag:
    ingest = PythonOperator(
        task_id='ingest_data',
        python_callable=lambda: print("Fetching raw crime data...")
    )

    process = PythonOperator(
        task_id='preprocess_data',
        python_callable=lambda: print("Cleaning and engineering features...")
    )

    predict = PythonOperator(
        task_id='predict_trends',
        python_callable=lambda: print("Running ML prediction models...")
    )

    ingest >> process >> predict