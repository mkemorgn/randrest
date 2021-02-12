import os
import requests
import json
import random
import numpy as np
from pprint import pprint
from dotenv import load_dotenv

#loads env variables
load_dotenv()

api_key = os.getenv("YELP_API_KEY")
headers = {'Authorization': 'Bearer %s' % api_key}

url='https://api.yelp.com/v3/businesses/search'

# In the dictionary, term can take values like food, cafes or businesses like McDonalds
location = input("Where do you want to search? ")
categories = input("If you have a certain type of food you want enter here " \
                   "(Optional press enter to skip.):")

params = {
    'term':'restaurants',
    'location': location,
    'categories': categories, 
    'radius': 16094,
    #'sort_by': 'rating',
    'open_now': True,
    #'limit': 5,
    }

def get_restaurant():
    # Making a get request to the API
    req=requests.get(url, params=params, headers=headers)

    # Making a get request to the API
    response=requests.get(url, params=params, headers=headers)

    #status code for debugging
    #print('The status code is {}'.format(req.status_code))
    
    data = response.json()
    
    # loops through json and returns business names
    name = data['businesses'][0]['name']
    
    arr = []
    for i in data['businesses']:
        restaurantList = i['name']
        
        arr.append(restaurantList)

    rand = random.choice(arr)
    print(rand)
    return;


