from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)

username = config['database']['mysql']['username']
password = config['database']['mysql']['password']
db = config['database']['mysql']['database']
host_port = config['database']['mysql']['host_port']


connection_string = 'mysql+pymysql://'+ username +':'+ password + '@' + host_port + '/' + db
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


if __name__ == "__main__":

    # from views import *

    # Add REST endpoints if needed
    print("\n")
    print ("Add REST endpoints if needed here, Else run the entry.py file for dataframe script")
    print("\n")

    app.run(debug=True)
