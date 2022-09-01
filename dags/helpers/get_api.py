import requests
 
def get_api(api):
  response = requests.get(api)
  response.json()
  game_popular_2022 = response.json()

  return game_popular_2022
