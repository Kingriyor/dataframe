import models
from tms_script import script # Function 1
from top_five import top_five_genres # Function 2


# I took the liberty of breaking the problem into seperate files, both of which i am calling here rather than a single file holding all the functions. 
# This was done to make the codebase more modular



# clear tables
print('\n')
print('Clearing existing records in tables if any ......')
script().clear_tables()
print('Done!')


# load table with new data from TMS (First function from question)
print('\n')
print('Updating database table contents ........')
script().getTVMovies()
script().getTheatreMovies()
print('Done!')

print('\n')

# NB if you want to use sample db (database/sample_25-10-2020_dataframe.sql) included in this repo, then comment everything above this comment to prevent current day's data from over-writing previous

# Run Pandas algorithm (Second function from question)
top_five_genres()

