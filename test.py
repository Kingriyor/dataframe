from app import db, connection_string
from sqlalchemy import create_engine
from config import config
import unittest
from datetime import datetime
import requests

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.base_url = config['tms']['base_url']
        self.api_key = config['tms']['key']
        self.lineupId = config['tms']['lineupId']
        self.zip_code = config['tms']['zip_code']
        self.startDateTime = datetime.today().strftime('%Y-%m-%d') # "2020-10-22"

    def test_db(self):
        connected = False
        try:
            db_connection = create_engine(connection_string)
            test_res = db_connection.execute("Select 1")
            connected = True
        except:
            print("Something is broken")
        
        self.assertTrue(connected)

    def test_tms_tvUrl(self):
        base_url = config['tms']['base_url']
        api_key = config['tms']['key']
        lineupId = config['tms']['lineupId']
        zip_code = config['tms']['zip_code']
        startDateTime = datetime.today().strftime('%Y-%m-%d')
        status_code = 404

        url = self.base_url + "/movies/airings?zip=" + self.zip_code + "&api_key=" + self.api_key + "&lineupId=" + self.lineupId + "&startDateTime=" + self.startDateTime
        try:
            response = requests.request("GET", url, headers={}, data = {})
        except:
            print ("Request failed")

        self.assertEqual(response.status_code, 200)

    def test_tms_theatreUrl(self):
        base_url = config['tms']['base_url']
        api_key = config['tms']['key']
        lineupId = config['tms']['lineupId']
        zip_code = config['tms']['zip_code']
        startDateTime = datetime.today().strftime('%Y-%m-%d')
        status_code = 404

        url = self.base_url + "/movies/showings?zip=" + self.zip_code + "&api_key=" + self.api_key + "&startDate=" + self.startDateTime
        try:
            response = requests.request("GET", url, headers={}, data = {})
        except:
            print ("Request failed")

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
