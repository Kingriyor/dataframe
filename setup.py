import models
from tms_script import script # Function 1



# create DB tables
print('\n')
print ("Creating database tables...")
models.execute()
print('Done!')

print('\n')


# update sql_mode
print('\n')
print ("Updating SQL mode...")
models.sql_mode()
print('Done!')

print('\n')