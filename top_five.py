import pandas as pd
import glob

#TODO - ensure movies with same tmsID are not counted as more than one for the count in dataframe

def read_file(file:str='')-> pd.DataFrame:
  if file.endswith(".csv"):
    dataframe = pd.read_csv(file)
  elif file.endswith(".json"):
    dataframe = pd.read_json(file)
  else:
    print('No file found. Ensure you pass a json/csv file')
  return dataframe

def explode_and_groupby(data:pd.DataFrame,groupby=True):
  data = data.explode('genres').reset_index(drop=True)
  if groupby:
    data = data[['genres','tmsId']].groupby('genres').count().sort_values(by=['tmsId'],ascending=False)
  return data

def top_five_movies():
  theatre = read_file('theatre_movies.json')
  movies = pd.read_json('tv_movies.json')
  movies = pd.concat([movies.drop(['program','ratings'],axis=1), movies.program.apply(pd.Series)],axis=1)
  joined_data = pd.concat([movies,theatre])[['title','releaseDate','genres','shortDescription','tmsId']]
  top5 = explode_and_groupby(joined_data).head(5)
  top5_list = list(top5.index)
  joined_data = explode_and_groupby(joined_data,groupby=False)
  condition = joined_data['genres'].isin(top5_list)
  final_data = joined_data[condition].reset_index(drop=True)
  return final_data

top_five_movies()