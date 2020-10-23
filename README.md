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

- update database section of config.py with your sql credentials

#### ---------------------------------- Option 1 ------------------------------------
```
- import the database export shared into your own DB (/database/dataframe.sql)
```

--------------------------------------------------------------------------------

#### ---------------------------------- Option 2 ------------------------------------
```
- create a db named 'dataframe'
```

- Run `models.py` file directly to create the database tables:

```
$ python models.py
```

You only need to do this once, unless you change your model definitions (see below).

--------------------------------------------------------------------------------




## Running the TMS script to load data in Database

```
$ python script.py
```


## Running the Dataframe script

```
$ python top_five.py
```


### Usefull 
Sql query
```
- SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
```
