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
        # response = requests.request("GET", url, headers={}, data = {})
        # # print(response.text.encode('utf8'))
        # print(response.json()[1])
        self.get_stream(url)

    def getTheatreMovies(self):
        url = self.base_url + "/movies/showings?zip=" + self.zip_code + "&api_key=" + self.api_key + "&startDate=" + self.startDateTime
        # response = requests.request("GET", url, headers={}, data = {})
        # # print(response.text.encode('utf8'))
        # print(response.json()[1])
        self.get_stream(url)

    def get_stream(self, url, headers=None):
        s = requests.Session()

        with s.get(url, headers=None, stream=True) as resp:
            for line in resp.iter_lines():
                if line:
                    print(line)




script().getTVMovies()
print("________________________________________________________________________________________")
script().getTheatreMovies()


