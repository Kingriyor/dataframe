import models
from tms_script import script
from top_five import top_five_genres


# I took the liberty of breaking the problem into seperate files all of which i am calling here rathere than a single file holding all the functions. 
# This was done to make the codebase more modular



# create DB tables
print('\n')
models.execute()

print('\n')

# clear tables
print('Clearing existing records in tables ......')
script().clear_tables()
print('Done!')


# reload table with new data from TMS (First function from question)
print('\n')
print('Updating database table contents ........')
script().getTVMovies()
script().getTheatreMovies()
print('Done!')

print('\n')

# Run Pandas algorithm (Second function from question)
top_five_genres()

