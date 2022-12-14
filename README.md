
# Best Games 2022

*First Project Data Pipeline*

## Building a simple ETL Data Pipeline 

### Introduction 

The key of data engineer is designing and building pipelines that transform and transport data into a desired format, when it reaches end users, it is in a highly usable state. These pipelines must take data from many disparate sources and collect them into a single warehouse that represents the data uniformly as a single source of truth. 

In this project, it's my first time to build ETL, I will take a few tools that I have studied. The goal of this project is to apply my knowledge of data engineers and the selection of tools to create ETL in entry-level.

### What is ETL?

The Extract, Transform, Load process (short: **ETL**) describes the steps between collection data from various sources to the point where it can finally be stored in a *data warehouse* solution.

### Used Technologies
- Docker and Docker-compose
- Airflow
- Python
- Visual studio code 
- pgAdmin 4 (PostgreSQL)

### Implementation
**step 1**

Create database in pgAdmin4.

![Create database](https://github.com/Little-BlackCat/best_game_2022/blob/main/Pics/Create%20Database.JPG)

Then, create Python script to build table and schemas for receiving data from extraction. The full script file is in [here](https://github.com/Little-BlackCat/best_game_2022/blob/main/dags/helpers/create_tables.py).

---
**step 2 : Extraction**

Next, create the data extractor Python scripts. The goal of these scripts are to create a data frame that can be loaded into warehouse using the PostgreSQL-connector-Python library. The full scripts file are found in [here](https://github.com/Little-BlackCat/best_game_2022/tree/main/dags).

---
**step 3 : Transformation**

The goal of this project is to find the best games of 2022, so the most important thing is the ratings from the sources. Having a high rating shows how popular the game is. The full script to find the best game is in [here](https://github.com/Little-BlackCat/best_game_2022/blob/main/dags/operators/merge_data.py).

---
**step 4 : Loading**

For this step create another script that will communicate with tables. the script file can be found [here](https://github.com/Little-BlackCat/best_game_2022/blob/main/dags/operators/update_table.py).

---
**step 5 : Aitflow Orchestration and Docker-compose**

The full dag script can be found [here](https://github.com/Little-BlackCat/best_game_2022/blob/main/dags/list_best_game_2022.py).

Ready to run the project. Follow step to run from [here](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)

---

### Reference
1. <https://rawg.io/>
2. <https://www.metacritic.com/>
3. <https://www.imdb.com/?ref_=nv_home>
4. <https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html>

