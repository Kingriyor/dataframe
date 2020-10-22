from app import db

class Theatre_movies(db.Model):
    # We always need an id
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))
    genres = db.Column(db.String(50))
    description = db.Column(db.String(200))
    theatre = db.Column(db.String(100))
    release_year = db.Column(db.Integer)

    def __init__(self, title, genres, description, theatre, release_year):
        self.title = title
        self.genres = genres
        self.description = description
        self.theatre = theatre
        self.release_year = release_year

class Tv_movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))
    genres = db.Column(db.String(50))
    description = db.Column(db.String(200))
    channel = db.Column(db.String(100))
    release_year = db.Column(db.Integer)

    def __init__(self, title, genres, description, channel, release_year):
        self.title = title
        self.genres = genres
        self.description = description
        self.channel = channel
        self.release_year = release_year


def create_movie(title, genres, description, release_year, theatre_or_channel, type='theatre'):
    # Note type must be ['theatre','tv']

    allowed_types = ['theatre','tv']
    if type.lower() not in allowed_types:
        return False

    if type.lower() == 'tv':
        movie = Tv_movies(title, genres, description, theatre_or_channel, release_year)
    else:
        movie = Theatre_movies(title, genres, description, theatre_or_channel, release_year)


    # Actually add this movie to the database
    db.session.add(movie)

    # Save all pending changes to the database
    db.session.commit()

    return movie


if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print "Creating database tables..."
    db.create_all()
    print "Done!"
