import os
import requests
import json
from pprint import pprint
from dotenv import load_dotenv

#loads env variables
load_dotenv()

api_key = os.getenv("YELP_API_KEY")
headers = {'Authorization': 'Bearer %s' % api_key}

url='https://api.yelp.com/v3/businesses/search'

# In the dictionary, term can take values like food, cafes or businesses like McDonalds
location = input("Where do you want to search? ")
params = {'term':'restaurants','location': location, 'limit':5}

def get_restaurant():
    # Making a get request to the API
    req=requests.get(url, params=params, headers=headers)

    # Making a get request to the API
    response=requests.get(url, params=params, headers=headers)

    #status code for debugging
    #print('The status code is {}'.format(req.status_code))


    data = response.json()
    #parsed_data = json.loads(req.text)
    #json_data = req.json()
    # loops through json and returns business names
    name = data['businesses'][0]['name']
    for i in data['businesses']:
        print(i['name'])
    #print("Your restaurant is: " + name)
    return;


