import models
from tms_script import script
from top_five import top_five_genres

print('\n')

# create DB tables
models.execute()

print('\n')

# clear tables
print('clearing existing records in tables ......')
script().clear_tables()
# reload table with new data from TMS

print('\n')
print('Updating Table contents ........')
script().getTVMovies()
script().getTheatreMovies()

print('\n')

# Run Pandas algorithm
top_five_genres()

