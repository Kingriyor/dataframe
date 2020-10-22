import requests
import json
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
        response = requests.request("GET", url, headers={}, data = {})
        if response.status_code != 200:
            print ("error occured")
            print (response.status_code)
        else:
            # print(response.text.encode('utf8'))
            json_response = response.json()
            size = len(json_response)
            for x in range(size):
                val = json_response[x]
                print(val)
                print("_________________________")
        

        # self.get_stream(url)

    def getTheatreMovies(self):
        url = self.base_url + "/movies/showings?zip=" + self.zip_code + "&api_key=" + self.api_key + "&startDate=" + self.startDateTime
        response = requests.request("GET", url, headers={}, data = {})
        if response.status_code != 200:
            print ("error occured")
            print (response.status_code)
        else:
            # print(response.text.encode('utf8'))
            json_response = response.json()
            size = len(json_response)
            for x in range(size):
                val = json_response[x]
                print(val)
                print("_________________________")

        # self.get_stream(url)

    # def get_stream(self, url, headers=None):
    #     s = requests.Session()

    #     with s.get(url, headers=None, stream=True) as resp:
    #         for line in resp.iter_lines():
    #             if line:
    #                 print(line)
    #                 # response_formated = json.loads(line)
    #                 # print(response_formated)
                    
    # def get_stream_chunk(self, url, headers=None):
    #     s = requests.Session()

    #     with s.get(url, headers=None, stream=True) as resp:
    #         for chunk in resp.iter_content(chunk_size=1):
    #             if chunk.endswith("\n"):
    #                 print(line.json())




script().getTVMovies()
# script().getTheatreMovies()


