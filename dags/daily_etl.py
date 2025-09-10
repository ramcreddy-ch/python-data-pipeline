from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    print("Extracting data...")

with DAG('daily_etl', start_date=datetime(2025, 1, 1)) as dag:
    t1 = PythonOperator(task_id='extract', python_callable=extract)
