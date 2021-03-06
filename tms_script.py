import requests
import json
from config import config
import models
from datetime import datetime



class script:
    def __init__(self):
        self.base_url = config['tms']['base_url']
        self.api_key = config['tms']['key']
        self.lineupId = config['tms']['lineupId']
        self.zip_code = config['tms']['zip_code']
        self.startDateTime = datetime.today().strftime('%Y-%m-%d') # "2020-10-22"

    def getTVMovies(self):
        url = self.base_url + "/movies/airings?zip=" + self.zip_code + "&api_key=" + self.api_key + "&lineupId=" + self.lineupId + "&startDateTime=" + self.startDateTime
        try:
            response = requests.request("GET", url, timeout=10, headers={}, data = {})
        except:
            print ("Request failed")
            return

        if response.status_code != 200:
            print ("error occured calling TMS TV MOVIES URL")
            print ("Status Code => " + str(response.status_code))
        else:
            # print(response.text.encode('utf8'))
            json_response = response.json()
            size = len(json_response)
            print("getTVMovies - " + str(size))
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
                release_year = val['program']['releaseYear'] if 'releaseYear' in val['program'] else 0

                
                meta_data = {
                    'startTime' : val['startTime'] if 'startTime' in val else "",
                    'endTime' : val['endTime'] if 'endTime' in val else "",
                    'duration' : val['duration'] if 'duration' in val else "",
                    'tmsId' : val['program']['tmsId'] if 'tmsId' in val['program'] else "",
                    'rootId' : val['program']['rootId'] if 'rootId' in val['program'] else "",
                    'releaseDate' : val['program']['releaseDate'] if 'releaseDate' in val['program'] else "",
                    'titleLang' : val['program']['titleLang'] if 'titleLang' in val['program'] else "",
                    'longDescription' : val['program']['longDescription'] if 'longDescription' in val['program'] else "",
                    'stationId' : val['stationId'] if 'stationId' in val else ""
                }

                # print(genres)

                # ALTERNATIVELY - send to rabbitmq and create a consumer to carry out the try-catch below
                try:
                    db_response = models.create_movie(title, genres, description, release_year, channel, 'tv', meta_data)
                    if db_response == False:
                        print ("error saving to DB")
                        # Then send current record to an error queue if needed
                except:
                    print ("error saving to DB")
                    # Then send current record to an error queue if needed


    def getTheatreMovies(self):
        url = self.base_url + "/movies/showings?zip=" + self.zip_code + "&api_key=" + self.api_key + "&startDate=" + self.startDateTime
        try:
            response = requests.request("GET", url, timeout=10, headers={}, data = {})
        except:
            print ("Request failed")
            return

        if response.status_code != 200:
            print ("error occured calling TMS THEATRE MOVIES URL")
            print ("Status Code => " + str(response.status_code))
        else:
            json_response = response.json()
            size = len(json_response)
            print("getTheatreMovies - " + str(size))
            for x in range(size):
                val = json_response[x]
                
                title = val['title']
                genres = ""
                if 'genres' in val:
                    genres_json = val['genres']
                    
                    for x in genres_json:
                        genres+=x
                        genres+=','
                description = val['shortDescription'] if 'shortDescription' in val else ""
                showtimes_json = val['showtimes']
                theatre_set = set()
                showtimes = ""

                for y in showtimes_json:
                    theatre_set.add(y['theatre']['id'])
                    showtimes += y['theatre']['id']
                    showtimes += '|'
                    showtimes += y['theatre']['name']
                    showtimes += '|'
                    showtimes += y['dateTime']

                theatre = ', '.join(str(e) for e in theatre_set)
                release_year = val['releaseYear'] if 'releaseYear' in val else 0

                
                meta_data = {
                    'showtimes' : showtimes,
                    'tmsId' : val['tmsId'],
                    'rootId' : val['rootId'],
                    'releaseDate' : val['releaseDate'] if 'releaseDate' in val else "",
                    'titleLang' : val['titleLang'] if 'titleLang' in val else "",
                    'longDescription' : val['longDescription'] if 'longDescription' in val else ""
                }

                # ALTERNATIVELY - send to rabbitmq and create a consumer to carry out the try-catch below
                try:
                    db_response = models.create_movie(title, genres, description, release_year, theatre, 'theatre', meta_data)
                    if db_response == False:
                        print ("error saving to DB")
                        # Then send current record to an error queue if needed
                except:
                    print ("error saving to DB")
                    # Then send current record to an error queue if needed



    def clear_tables(self):
        models.clear_table_contents()




