import os
import pandas as pd
import psycopg2
from helpers.execute_values import execute_values

def update_table():
    conn = psycopg2.connect(
	dbname = os.getenv("dbname"),
        user = os.getenv("user"),
        password = os.getenv("password"),
        host = os.getenv("host"),
        port = 5432
    )

    df = pd.read_csv("/home/airflow/data/list_best_game_2022.csv")
    execute_values(conn, df, 'best_games')

