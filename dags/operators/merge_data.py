import pandas as pd

# Merge 3 DataFrame
def merge_data():
    best_video_games = pd.read_csv("/home/airflow/data/best_video_games_2022.csv")
    video_game_released = pd.read_csv("/home/airflow/data/video_game_released_2022.csv")
    rawg_game_list = pd.read_csv("/home/airflow/data/rawg_game_list_2022.csv")

    final_df1 = rawg_game_list.merge(video_game_released, how="left", left_on="Name", right_on="Game")
    final_df = final_df1.merge(best_video_games, how="left", on = "Game")

    dup_df = final_df.drop_duplicates(subset = ["Name"], keep = "last")
    drop_year = dup_df.dropna(subset=["Years"])
    drop_df = drop_year.drop(columns = ["Game", "Released"])
    final_df = drop_df.reset_index().drop(columns = ['index'])
    list_best_game_2022 = final_df[["ID", "Name", "Platform", "Genre", "Directors", "Stars", "Years", "Metacritic", "Rating", "IMDB", "Votes", "Metascore", "User_score"]]

    list_best_game_2022.to_csv("/home/airflow/data/list_best_game_2022.csv", index = False)