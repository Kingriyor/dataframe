from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from config import config

username = config['database']['mysql']['username']
password = config['database']['mysql']['password']
db = config['database']['mysql']['database']
host_port = config['database']['mysql']['host_port']


connection_string = 'mysql+pymysql://'+ username +':'+ password + '@' + host_port + '/' + db
db_connection = create_engine(connection_string)
meta = MetaData()


theatre_movies = Table(
    'theatre_movies', meta, 
    Column('id', Integer, primary_key = True), 
    Column('title', String(100)), 
    Column('genres', String(100)),
    Column('description', String(200)),
    Column('theatre', String(100)),
    Column('release_year', Integer),
    Column('showtimes', String(1000)),
    Column('tmsId', String(15)),
    Column('rootId', String(100)),
    Column('releaseDate', String(50)),
    Column('titleLang', String(100)),
    Column('longDescription', String(500)),
)

tv_movies = Table(
    'tv_movies', meta, 
    Column('id', Integer, primary_key = True), 
    Column('title', String(100)), 
    Column('genres', String(100)),
    Column('description', String(200)),
    Column('channel', String(100)),
    Column('release_year', Integer),
    Column('startTime', String(100)),
    Column('endTime', String(100)),
    Column('duration', String(100)),
    Column('tmsId', String(15)),
    Column('rootId', String(100)),
    Column('releaseDate', String(50)),
    Column('titleLang', String(100)),
    Column('longDescription', String(500)),
    Column('stationId', String(100)),
)

def execute():
    db_connection.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
    meta.create_all(db_connection)

def create_movie(title, genres, description, release_year, theatre_or_channel, type='theatre', meta_data={}):
    allowed_types = ['theatre','tv']
    if type.lower() not in allowed_types:
        return False

    if type.lower() == 'tv':
        stmt = tv_movies.insert().values(
            title = title,
            genres = genres,
            description = description,
            channel = theatre_or_channel,
            release_year = release_year,
            startTime = meta_data['startTime'] if 'startTime' in meta_data else "",
            endTime = meta_data['endTime'] if 'endTime' in meta_data else "",
            duration = meta_data['duration'] if 'duration' in meta_data else "",
            tmsId = meta_data['tmsId'] if 'tmsId' in meta_data else "",
            rootId = meta_data['rootId'] if 'rootId' in meta_data else "",
            releaseDate = meta_data['releaseDate'] if 'releaseDate' in meta_data else "",
            titleLang = meta_data['titleLang'] if 'titleLang' in meta_data else "",
            longDescription = meta_data['longDescription'] if 'longDescription' in meta_data else "",
            stationId = meta_data['stationId'] if 'stationId' in meta_data else ""
            )

    else:
        stmt = theatre_movies.insert().values(
            title = title,
            genres = genres,
            description = description,
            theatre = theatre_or_channel,
            release_year = release_year,
            showtimes = meta_data['showtimes'] if 'showtimes' in meta_data else "",
            tmsId = meta_data['tmsId'] if 'tmsId' in meta_data else "",
            rootId = meta_data['rootId'] if 'rootId' in meta_data else "",
            releaseDate = meta_data['releaseDate'] if 'releaseDate' in meta_data else "",
            titleLang = meta_data['titleLang'] if 'titleLang' in meta_data else "",
            longDescription = meta_data['longDescription'] if 'longDescription' in meta_data else ""
            )

    # Actually add this movie to the database
    db_connection.execute(stmt)
    return True

def clear_table_contents():
    stmt1 = theatre_movies.delete()
    stmt2 = tv_movies.delete()
    db_connection.execute(stmt1)
    db_connection.execute(stmt2)

