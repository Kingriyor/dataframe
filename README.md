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

## Running the Dataframe script

```
$ python entry.py
```

