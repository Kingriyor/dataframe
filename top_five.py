import pandas as pd
import glob
from app import connection_string
from sqlalchemy import create_engine


# TODO - ensure movies with same tmsID are not counted as more than one for the count in dataframe

def read_file(file: str = '') -> pd.DataFrame:
    # This function gets a dataframe from a json file
    if file.endswith(".csv"):
        dataframe = pd.read_csv(file)
    elif file.endswith(".json"):
        dataframe = pd.read_json(file)
    else:
        print('No file found. Ensure you pass a json/csv file')
    return dataframe


def read_db(table_name) -> pd.DataFrame:
    # This function gets a dataframe from a database table
    db_connection = create_engine(connection_string)
    query_string = ''

    if table_name == 'theatre_movies':
        query_string = "SELECT title, releaseDate, genres,description, tmsId, GROUP_CONCAT(theatre, ',') AS theatres FROM " + table_name + " GROUP BY tmsId"

    elif table_name == 'tv_movies':
        query_string = "SELECT title, releaseDate, genres,description, tmsId, GROUP_CONCAT(channel, ',') AS channels FROM " + table_name + " GROUP BY tmsId"

    else:
        query_string = "SELECT * FROM " + table_name

    # print(query_string)

    df = pd.read_sql(query_string, con=db_connection)

    return df


def explode_and_groupby(data: pd.DataFrame, groupby=True):
    # TODO look into this, its not exploding comma seperated
    data = data.explode('genres').reset_index(drop=True)
    if groupby:
        data = data[['genres', 'tmsId']].groupby(
            'genres').count().sort_values(by=['tmsId'], ascending=False)
    return data


def top_five_movies():
    # theatre = read_file('theatre_movies.json')
    # movies = pd.read_json('tv_movies.json')

    theatre = read_db('theatre_movies')
    movies = read_db('tv_movies')

    # remove multiple commas
    theatre['theatres'] = theatre['theatres'].map(lambda x: x.replace(',,', ','))
    movies['channels'] = movies['channels'].map(lambda x: x.replace(',,', ','))

    # make genres a list
    theatre['genres'] = theatre['genres'].map(lambda x: x.strip(',').split(','))
    movies['genres'] = movies['genres'].map(lambda x: x.strip(',').split(','))



    # Group both the Movie lists based on ‘Genre’ ------------------------------------------------------------------------------------------------
    theatre_genre_group = explode_and_groupby(theatre, groupby=True)
    print('\n theatre_genre_groups \n')
    print(theatre_genre_group)
    print('\n\n')

    tv_genre_group = explode_and_groupby(movies, groupby=True)
    print('\n tv_genre_groups \n')
    print(tv_genre_group)
    print('\n\n')

    # Group both the Movie lists based on ‘Genre’ ------------------------------------------------------------------------------------------------ 61


    # Combine the movie lists (Theatre and Channel movies) based on the Genres ------------------------------------------------------------------------------------------------
    joined_data = pd.concat([movies, theatre])[
        ['title', 'releaseDate', 'genres', 'description', 'tmsId', 'theatres', 'channels']]


    # Return the Top 5 Genres with the highest movie count along with the movie details ------------------------------------------------------------------------------------------------
    top5 = explode_and_groupby(joined_data).head(5)
    print('\n top5 \n')
    print(top5)
    print('\n\n')

    top5_list = list(top5.index)
    joined_data = explode_and_groupby(joined_data, groupby=False)
    condition = joined_data['genres'].isin(top5_list)
    final_data = joined_data[condition].reset_index(drop=True)
    final_data = final_data.sort_values('genres')
    # final_data.drop_duplicates(keep='first',inplace=True, subset="tmsId")

    print('\n movie details for top5 \n')
    print(final_data)
    print('\n\n')

    return final_data


top_five_movies()
