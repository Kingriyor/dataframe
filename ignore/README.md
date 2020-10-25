## Installing Dependencies

Python 3.8

```
pip install -r requirements.txt
```

If you need to add new packages
```
pip install package && pip freeze > requirements.txt
```


## Database Setup

1) update database section of config.py with your sql credentials


2) create DB

```
- import the database export shared into your own DB (/database/dataframe.sql)

OR

- create an SQL db named 'dataframe'
```

3) create tables in DB

- Run `models.py` file directly to create the database tables:

```
$ python models.py
```

You only need to do this once, unless you change your model definitions

--------------------------------------------------------------------------------




## Running the TMS script to load data in Database

```
$ python script.py
```


## Running the Dataframe script

```
$ python top_five.py
```

