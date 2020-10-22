import requests
from config import config


class script:
    def __init__(self):
        self.base_url = config['tms']['base_url']
        self.api_key = config['tms']['key']
        self.lineupId = config['tms']['lineupId']
        self.zip_code = config['tms']['zip_code']
        self.startDateTime = "2020-10-22" # current date

    def getTVMovies(self):
        url = self.base_url + "/movies/airings?zip=" + self.zip_code + "&api_key=" + self.api_key + "&lineupId=" + self.lineupId + "&startDateTime=" + self.startDateTime
        payload = {}
        headers= {}
        response = requests.request("GET", url, headers=headers, data = payload)
        # print(response.text.encode('utf8'))
        print(response.json()[1])

    def getTheatreMovies(self):
        url = self.base_url + "/movies/showings?zip=" + self.zip_code + "&api_key=" + self.api_key + "&line_up_id=" + self.lineupId + "&startDate=" + self.startDateTime
        payload = {}
        headers= {}
        response = requests.request("GET", url, headers=headers, data = payload)
        # print(response.text.encode('utf8'))
        print(response.json()[1])



script().getTVMovies()

