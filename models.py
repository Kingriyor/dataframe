from app import db

class Theatre_movies(db.Model):
    # We always need an id
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))
    genres = db.Column(db.String(100))
    description = db.Column(db.String(200))
    theatre = db.Column(db.String(100)) # comma_seperated theatre id (from showtimes)
    release_year = db.Column(db.Integer)

    showtimes = db.Column(db.String(1000)) #json to string
    # tmsId = db.Column(db.String(100), unique=True)
    tmsId = db.Column(db.String(100))
    rootId = db.Column(db.String(100))
    releaseDate = db.Column(db.String(100)) 
    titleLang = db.Column(db.String(100))
    longDescription = db.Column(db.String(500))


    def __init__(self, title, genres, description, theatre, release_year, meta_data = {}):
        self.title = title
        self.genres = genres
        self.description = description
        self.theatre = theatre
        self.release_year = release_year

        self.showtimes = meta_data['showtimes'] if 'showtimes' in meta_data else ""
        # self.duration = meta_data['duration'] if 'duration' in meta_data else ""
        self.tmsId = meta_data['tmsId'] if 'tmsId' in meta_data else ""
        self.rootId = meta_data['rootId'] if 'rootId' in meta_data else ""
        self.releaseDate = meta_data['releaseDate'] if 'releaseDate' in meta_data else ""
        self.titleLang = meta_data['titleLang'] if 'titleLang' in meta_data else ""
        self.longDescription = meta_data['longDescription'] if 'longDescription' in meta_data else ""

class Tv_movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))
    genres = db.Column(db.String(100)) #pass as comma seperated string
    description = db.Column(db.String(200))
    channel = db.Column(db.String(100))
    release_year = db.Column(db.Integer)

    startTime = db.Column(db.String(100))
    endTime = db.Column(db.String(100))
    duration = db.Column(db.String(100))
    # tmsId = db.Column(db.String(100), unique=True)
    tmsId = db.Column(db.String(100))
    rootId = db.Column(db.String(100))
    releaseDate = db.Column(db.String(100))
    titleLang = db.Column(db.String(100))
    longDescription = db.Column(db.String(500))
    stationId = db.Column(db.String(100))



    def __init__(self, title, genres, description, channel, release_year, meta_data = {}):
        self.title = title
        self.genres = genres
        self.description = description
        self.channel = channel
        self.release_year = release_year

        self.startTime = meta_data['startTime'] if 'startTime' in meta_data else ""
        self.endTime = meta_data['endTime'] if 'endTime' in meta_data else ""
        self.duration = meta_data['duration'] if 'duration' in meta_data else ""
        self.tmsId = meta_data['tmsId'] if 'tmsId' in meta_data else ""
        self.rootId = meta_data['rootId'] if 'rootId' in meta_data else ""
        self.releaseDate = meta_data['releaseDate'] if 'releaseDate' in meta_data else ""
        self.titleLang = meta_data['titleLang'] if 'titleLang' in meta_data else ""
        self.longDescription = meta_data['longDescription'] if 'longDescription' in meta_data else ""
        self.stationId = meta_data['stationId'] if 'stationId' in meta_data else ""
        



def create_movie(title, genres, description, release_year, theatre_or_channel, type='theatre', meta_data={}):
    # Note type must be ['theatre','tv']

    allowed_types = ['theatre','tv']
    if type.lower() not in allowed_types:
        return False

    if type.lower() == 'tv':
        movie = Tv_movies(title, genres, description, theatre_or_channel, release_year, meta_data)
    else:
        movie = Theatre_movies(title, genres, description, theatre_or_channel, release_year, meta_data)


    # Actually add this movie to the database
    db.session.add(movie)

    # Save all pending changes to the database
    db.session.commit()

    return movie


if __name__ == "__main__":
    #TODO - ensure movies with same tmsID are not counted as more than one for the count in dataframe

    # Run this file directly to create the database tables.
    print "Creating database tables..."
    db.create_all()
    print "Done!"
