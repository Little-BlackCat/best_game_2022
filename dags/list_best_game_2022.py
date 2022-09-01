from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

from operators import best_game, list_game, merge_data, update_table, video_game_released
from helpers.create_tables import create_tables

# Create DAG
default_args = {
    'owner': 'blackcat',
    'depends_on_past': False,
    'catchup': False,
    'start_date': days_ago(0),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'Retail_pipeline',
    default_args=default_args,
    description='Pipeline for ETL online_retail data',
    schedule_interval=timedelta(days=1),
)

# Tasks
t1 = PythonOperator(
    task_id = "wep_scraping1",
    python_callable = best_game,
    dag = dag
    
)

t2 = PythonOperator(
    task_id = "wep_scraping2",
    python_callable = video_game_released,
    dag = dag
    
)

t3 = PythonOperator(
    task_id = "api_call",
    python_callable = list_game,
    dag = dag
    
)

t4 = PythonOperator(
    task_id = "merge_data",
    python_callable = merge_data,
    dag = dag
    
)

t5 = PythonOperator(
    task_id = "create_table",
    python_callable = create_tables,
    dag = dag
    
)

t6 = PythonOperator(
    task_id = "fill_data",
    python_callable = update_table,
    dag = dag
    
)

# Dependencies

[t1, t2, t3, t5] >> t4 >> t6