## Installing Dependencies

- Python 3.8
- Pipenv
- SQL database server


## Database Setup

1) update database section of config.py with your sql credentials


2) create DB

```
- import the database export shared(/database/dataframe.sql) into your own DB 

OR

- create an SQL db named 'dataframe'
```


# Environment setup

```
- $ pipenv install
```

```
- $ pipenv shell
```

## Running the unittest

```
$ python test.py
```

## Running the Dataframe script

```
$ python entry.py
```


#### NB if you want to use sample db (database/sample_25-10-2020_dataframe.sql) included in this repo, then follow the instruction in entry.py to prevent current day's data from over-writing previous

