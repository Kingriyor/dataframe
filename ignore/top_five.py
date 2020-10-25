import pandas as pd
import glob
from app import connection_string
from sqlalchemy import create_engine


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
        query_string = "SELECT title, releaseDate, genres,description, tmsId, GROUP_CONCAT(theatre, ',') AS theatre_Ids FROM " + table_name + " GROUP BY tmsId"

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


def top_five_genres():
    # theatre = read_file('theatre_movies.json')
    # movies = pd.read_json('tv_movies.json')

    theatre = read_db('theatre_movies')
    movies = read_db('tv_movies')

    # remove multiple commas in the 'theatre_Ids' and 'channels' columns
    theatre['theatre_Ids'] = theatre['theatre_Ids'].map(lambda x: x.replace(',,', ','))
    movies['channels'] = movies['channels'].map(lambda x: x.replace(',,', ','))

    # convert genres to a lists from comma-seperated strings
    theatre['genres'] = theatre['genres'].map(lambda x: x.strip(',').split(','))
    movies['genres'] = movies['genres'].map(lambda x: x.strip(',').split(','))



    # Group the Movie and Theatre list based on ‘Genres’ ------------------------------------------------------------------------------------------------
    theatre_genre_group = explode_and_groupby(theatre, groupby=True)
    # print('\n theatre_genre_groups \n')
    # print(theatre_genre_group)
    # print('\n\n')

    tv_genre_group = explode_and_groupby(movies, groupby=True)
    # print('\n tv_genre_groups \n')
    # print(tv_genre_group)
    # print('\n\n')

    # ---------------------------------------------------------------------------------------------------------------------------------------------------


    # Combine the movie lists (Theatre and Channel movies)  ------------------------------------------------------------------------------------------------
    joined_data = pd.concat([movies, theatre])[
        ['title', 'releaseDate', 'genres', 'description', 'tmsId', 'theatre_Ids', 'channels']]


    # Group combined data based on the Genres and Return the Top 5 Genres with the highest movie count along with the movie details ------------------------------------------------------------------------------------------------
    top5 = explode_and_groupby(joined_data).head(5)
    print('\n top5 \n')
    print(top5)
    print('\n\n')

    top5_list = list(top5.index)
    joined_data = explode_and_groupby(joined_data, groupby=False)
    condition = joined_data['genres'].isin(top5_list)
    top5_movies_details = joined_data[condition].reset_index(drop=True)
    top5_movies_details = top5_movies_details.sort_values('genres')
    # final_data.drop_duplicates(keep='first',inplace=True, subset="tmsId")

    print('\n movie details for top5 \n')
    print(top5_movies_details)
    print('\n\n')

    return top5

# Run infile
# top_five_genres()
