import requests
from config import config

base_url = config['tms']['base_url']
api_key = config['tms']['key']
lineupId = config['tms']['lineupId']
zip_code = config['tms']['zip_code']
startDateTime = "2020-10-22" # current date

# TV 
# url = base_url + "/movies/airings?zip=" + zip_code + "&api_key=" + api_key + "&lineupId=" + lineupId + "&startDateTime=" + startDateTime

# Theatre
url = base_url + "/movies/showings?zip=" + zip_code + "&api_key=" + api_key + "&line_up_id=" + lineupId + "&startDate=" + startDateTime



payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))

print(response.json()[1])
