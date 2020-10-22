import requests
import json
from config import config
import models


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
                
                title = val['program']['title']
                genres_json = val['program']['genres']
                genres = ""
                for x in genres_json:
                    genres+=x
                    genres+=','
                description = val['program']['shortDescription'] if 'shortDescription' in val['program'] else ""
                channel = val['station']['channel']
                release_year = val['program']['releaseYear']

                
                meta_data = {
                    'startTime' : val['startTime'],
                    'endTime' : val['endTime'],
                    'duration' : val['duration'],
                    'tmsId' : val['program']['tmsId'],
                    'rootId' : val['program']['rootId'],
                    'releaseDate' : val['program']['releaseDate'],
                    'titleLang' : val['program']['titleLang'],
                    'longDescription' : val['program']['longDescription'],
                    'stationId' : val['stationId']
                }

                # print(genres)

                models.create_movie(title, genres, description, release_year, channel, 'tv', meta_data)




                
        

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

# models.create_movie("test", "Comedy drama,Dark comedy", "A TV star and his longtime stunt double make their way around a changing industry in 1969 Hollywood.", "2019", "582", "tv", {"tmsId": "MV010921590000", "rootId": "15226224","subType": "Feature Film",})


