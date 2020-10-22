from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)


# username = 'root'
# password = 'root'
# db = 'dataframe'
# host_port = 'localhost:8889'

username = config['database']['mysql']['username']
password = config['database']['mysql']['password']
db = config['database']['mysql']['database']
host_port = config['database']['mysql']['host_port']



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+ username +':'+ password + '@' + host_port + '/' + db
db = SQLAlchemy(app)


if __name__ == "__main__":

    # from views import *

    app.run(debug=True)
