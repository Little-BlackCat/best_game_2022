import os
import pandas as pd
import psycopg2
from helpers.execute_values import execute_values

def update_table():
    conn = psycopg2.connect(
<<<<<<< HEAD
        dbname = os.getenv("dbname"),
=======
	dbname = os.getenv("dbname"),
>>>>>>> c7374b98995a98154ca1eb9193ede1f73ad2e96a
        user = os.getenv("user"),
        password = os.getenv("password"),
        host = os.getenv("host"),
        port = 5432
    )

    df = pd.read_csv("/home/airflow/data/list_best_game_2022.csv")
    execute_values(conn, df, 'best_games')

