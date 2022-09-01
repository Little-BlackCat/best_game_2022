import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#Web Scraping
def best_game():
  pages = [str(i) for i in range(5)]
  #Lists to store the scraped data in
  s = requests.Session()
  s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
  
  names = []
  game_platform = []
  years = []
  metascore = []
  user_score = []

  for page in pages:
    url = "https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?view=detailed&page={}".format(page)
    response = s.get(url)
    html_soup = BeautifulSoup(response.text, "html.parser")
    game_containers = html_soup.find_all("td", class_ = "clamp-summary-wrap")

    #Extract data from infividual movie container
    for container in game_containers:

    #The Name
      if container.h3 is not None:
        name = container.h3.text
        names.append(name)
      else:
        names.append(None)
      
    #The Platform
      if container.find("span", class_ = "data") is not None:
        platform = container.find("span", class_ = "data").text
        platform = re.sub(r"^\s+|\s+$", "", platform)
        game_platform.append(platform)
      else:
        game_platform.append(None)

    #The year
      if container.find("span", class_ = "") is not None:
        year = container.find("span", class_ = "").text
        years.append(year)
      else:
        years.append(None)

    #The Metascore
      if container.find("div", class_ = "metascore_w large game positive") is not None:
        meta = container.find("div", class_ = "metascore_w large game positive").text
        metascore.append(int(meta))
      elif container.find("div", class_ = "metascore_w large game mixed") is not None:
        meta = container.find("div", class_ = "metascore_w large game mixed").text
        metascore.append(int(meta))
      elif container.find("div", class_ = "metascore_w large game negative") is not None:
        meta = container.find("div", class_ = "metascore_w large game negative").text
        metascore.append(int(meta))
      else:
        metascore.append(None)
      
    #The User score
      if container.find("div", class_ = "metascore_w user large game positive") is not None:
        user = container.find("div", class_ = "metascore_w user large game positive").text
        user_score.append(float(user))
      elif container.find("div", class_ = "metascore_w user large game mixed") is not None:
        user = container.find("div", class_ = "metascore_w user large game mixed").text
        user_score.append(float(user))
      elif container.find("div", class_ = "metascore_w user large game negative") is not None:
        user = container.find("div", class_ = "metascore_w user large game negative").text
        user_score.append(float(user))
      else:
        user_score.append(None)


  games_df = pd.DataFrame({
    "Game" : names,
    "Platform" : game_platform,
    "Years" : years,
    "Metascore" : metascore,
    "User_score" : user_score
  })

  games_df["Years"] = pd.to_datetime(games_df["Years"]).dt.date
  games_df.to_csv("/home/airflow/data/best_video_games_2022.csv", index = False)