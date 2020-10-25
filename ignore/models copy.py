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




# class Dessert(db.Model):
#     # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
#     # for details on the column types.

#     # We always need an id
#     id = db.Column(db.Integer, primary_key=True)

#     # A dessert has a name, a price and some calories:
#     name = db.Column(db.String(100))
#     price = db.Column(db.Float)
#     calories = db.Column(db.Integer)

#     def __init__(self, name, price, calories):
#         self.name = name
#         self.price = price
#         self.calories = calories

#     def calories_per_dollar(self):
#         if self.calories:
#             return self.calories / self.price


# class Menu(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))

#     def __init__(self, name):
#         self.name = name


# def create_dessert(new_name, new_price, new_calories):
#     # Create a dessert with the provided input.
#     # At first, we will trust the user.

#     # This line maps to line 16 above (the Dessert.__init__ method)
#     dessert = Dessert(new_name, new_price, new_calories)

#     # Actually add this dessert to the database
#     db.session.add(dessert)

#     # Save all pending changes to the database
#     db.session.commit()

#     return dessert


if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print "Creating database tables..."
    db.create_all()
    print "Done!"
