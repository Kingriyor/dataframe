### Installing Dependencies

Python 3.8

```
pip install -r requirements.txt
```

If you need to add new packages
```
pip install package && pip freeze > requirements.txt
```

### Running the App

- create a db named 'dataframe'

- To run the app, first run the `models.py` file directly to create the database tables:

```
$ python models.py
```

You only need to do this once, unless you change your model definitions (see below).

Then run the app itself:

```
$ python script.py
```


TODO - ensure movies with same tmsID are not counted as more than one for the count in dataframe



1) - divide it to have
tv_movies horror , theatre_movies horror , tv_movies comedy, theatre_movies comedy ....... etc

2) - add them 
comedy = tv_movies comedy + theatre_movies comedy
horror = tv_movies horror + theatre_movies horror

3) get count for comedy, horror ...... etc
get highest 5 genres alongside the movies that fall under them
