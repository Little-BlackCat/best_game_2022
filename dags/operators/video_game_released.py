import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#Web Scraping
pages = [str(i) for i in range(1, 551, 50)]
#Lists to store the scraped data in
names = []
genre = []
imdb_ratings = []
directors = []
stars = []
votes = []

def video_game_released():
  for page in pages:
    url = "https://www.imdb.com/search/title/?title_type=video_game&release_date=2022-01-01,2022-12-31&start={}&ref_=adv_nxt".format(page)
    response = requests.get(url)
    html_soup = BeautifulSoup(response.text, "html.parser")
    game_containers = html_soup.find_all("div", class_ = "lister-item mode-advanced")

    #Extract data from infividual movie container
    for container in game_containers:

    #The IMDB rating
      if container.strong is not None:
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)
      else:
        imdb_ratings.append(None)

    #The Name
      if container.h3.a is not None:
        name = container.h3.a.text
        names.append(name)
      else:
        names.append(None)

    #The Genre
      if container.p.find("span", class_ = "genre") is not None:
        genre_ = container.p.find("span", class_ = "genre").text
        genre_ = re.sub(r"\s+$", "", genre_)
        genre.append(genre_[1:])
      else:
        genre.append(None)

    #The Director
      directors_tmp = []
      directors_string = ""
      for name in container.find('p', class_ =""):
        directors_tmp.append(name.get_text(strip=True))

      res_direc = [x for x in directors_tmp if re.search("Direc", x)]
      if res_direc != []:
        for i in range(1, len(directors_tmp)):
          if directors_tmp[i] == ',':
            pass
          elif directors_tmp[i] == '':
            break
          else:
            directors_string += directors_tmp[i]+', '
        directors.append(directors_string)
      else:
        directors.append(None)
        

    #The Stars
      stars_tmp = []
      stars_string = ""
      tmp = container.find('p', class_='')
      for i in tmp:
        stars_tmp.append(i.get_text(strip=True))
      
      if 'Stars:' in stars_tmp:
        for i in range(stars_tmp.index('Stars:') + 1, len(stars_tmp)):
          if stars_tmp[i] == ',':
            pass
          elif stars_tmp[i] == '':
            break
          else:
            stars_string += stars_tmp[i]+', '
        stars.append(stars_string)
      else:
        stars.append(None)
        
    #The Vote
      if container.find("span", attrs = {"name":"nv"}) is not None:
        vote = container.find("span", attrs = {"name":"nv"})["data-value"]
        votes.append(int(vote))
      else:
        votes.append(None)

  games_df = pd.DataFrame({
      "Game" : names,
      "Genre" : genre,
      "Directors" : directors,
      "Stars" : stars,
      "IMDB" : imdb_ratings,
      "Votes" : votes
  })
    
  games_df.to_csv("/home/airflow/data/video_game_released_2022.csv", index = False)