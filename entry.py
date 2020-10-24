import models
from tms_script import script
from top_five import top_five_genres

# create DB tables
models.execute()

# clear tables
script().clear_tables()
# reload table with new data from TMS
script().getTVMovies()
script().getTheatreMovies()

# Run Pandas algorithm
top_five_genres()

