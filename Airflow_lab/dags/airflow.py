import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.etl import extract_data, transform_data, load_data, analyze_data

default_args = {
    'owner': 'Harshit Kumar Taneja',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=3)
}

with DAG(
    'Crypto_ETL_Pipeline',
    default_args=default_args,
    description='ETL Pipelimne Using Airflow',
    schedule=None,
    catchup=False,    
) as dag:

    extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        op_args=[extract.output],
    )

    load = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
        op_args=[transform.output],
    )

    analyze = PythonOperator(
        task_id='analyze_data',
        python_callable=analyze_data,
        op_args=[load.output],
    )

    extract >> transform >> load >> analyze
