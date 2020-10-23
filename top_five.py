import pandas as pd
import glob
from app import connection_string
from sqlalchemy import create_engine


#TODO - ensure movies with same tmsID are not counted as more than one for the count in dataframe

def read_file(file:str='')-> pd.DataFrame:
  if file.endswith(".csv"):
    dataframe = pd.read_csv(file)
  elif file.endswith(".json"):
    dataframe = pd.read_json(file)
  else:
    print('No file found. Ensure you pass a json/csv file')
  return dataframe

def read_db(table_name)-> pd.DataFrame:
  db_connection = create_engine(connection_string)
  query_string = ''

  if table_name == 'theatre_movies':
    query_string = "SELECT title, releaseDate, genres,description, tmsId, GROUP_CONCAT(theatre, ',') AS theatres FROM " + table_name + " GROUP BY tmsId"
    
  else:
    query_string = "SELECT title, releaseDate, genres,description, tmsId, GROUP_CONCAT(channel, ',') AS channels FROM " + table_name + " GROUP BY tmsId"

  print(query_string)
  
  df = pd.read_sql(query_string, con=db_connection)

  # print(df)
  return df

def explode_and_groupby(data:pd.DataFrame,groupby=True):
  data = data.explode('genres').reset_index(drop=True)
  if groupby:
    data = data[['genres','tmsId']].groupby('genres').count().sort_values(by=['tmsId'],ascending=False)
  return data

def top_five_movies():
  # theatre = read_file('theatre_movies.json')
  # movies = pd.read_json('tv_movies.json')

  theatre = read_db('theatre_movies')
  movies = read_db('tv_movies')

  # remove multiple commas
  theatre['theatres'] = theatre['theatres'].map(lambda x: x.replace(',,',','))
  movies['channels'] = movies['channels'].map(lambda x: x.replace(',,',','))

  # movies = pd.concat([movies.drop(['program','ratings'],axis=1), movies.program.apply(pd.Series)],axis=1)

  joined_data = pd.concat([movies,theatre])[['title','releaseDate','genres','description','tmsId','theatres','channels']]
  top5 = explode_and_groupby(joined_data).head(5)
  print(top5)
  top5_list = list(top5.index)
  joined_data = explode_and_groupby(joined_data,groupby=False)
  condition = joined_data['genres'].isin(top5_list)
  final_data = joined_data[condition].reset_index(drop=True)
  # final_data.drop_duplicates(keep='first',inplace=True, subset="tmsId")
  print (final_data)
  return final_data

top_five_movies()