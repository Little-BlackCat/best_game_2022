import os
import psycopg2
# from dotenv import load_dotenv
# load_dotenv(".env")

def create_tables():
    """create tables in the PostgreSQL database"""
    commands = (
    '''CREATE TABLE Best_Games(
        ID INTEGER PRIMARY KEY,
        Name VARCHAR(255),
        Platform CHAR(20),
        Genre VARCHAR(255),
        Directors VARCHAR(255),
        Stars VARCHAR(255),
        Years DATE,
        Metacritic REAL,
        Rating REAL,
        IMDB REAL,
        Votes REAL,
        Metascore REAL,
        User_score REAL
    )'''
    )

    conn = None
    try:
    # connect to the PostgreSQL server
        conn = psycopg2.connect(
            dbname = os.getenv("dbname"),
            user = os.getenv("user"),
            password = os.getenv("password"),
            host = os.getenv("host"),
            port = 5432
        )
        cur = conn.cursor()
        # create table
        cur.execute(commands)

        # close communication with the PostgreSQL database server
        cur.close()

        # commit the changes
        conn.commit()
        print('Process Done!')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()



    
