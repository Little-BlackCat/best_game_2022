import os
import pandas as pd
from helpers.get_api import get_api

# Get API
api_key = os.getenv("api_key")

def list_game():
  game_popular_2022 = get_api(api_key)
  id = []
  name = []
  metacritic = []
  rating = []
  released = []
  i = 0
  while i < 50:
    for list_game in game_popular_2022["results"]:
      id.append(list_game["id"])
      name.append(list_game["name"])
      metacritic.append(list_game["metacritic"])
      rating.append(list_game["rating"])
      released.append(list_game["released"])
    
    game_popular_2022 = get_api(game_popular_2022["next"])
    i += 1  
    

  df_game = pd.DataFrame({
    "ID" : id,
    "Name" : name,
    "Metacritic" : metacritic,
    "Rating" : rating,
    "Released" : released
  })

  df_game.to_csv("/home/airflow/data/rawg_game_list_2022.csv", index = False)