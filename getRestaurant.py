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
params = {'term':'seafood','location':'New York City'}

def get_restaurant():
    # Making a get request to the API
    req=requests.get(url, params=params, headers=headers)

    # Making a get request to the API
    req=requests.get(url, params=params, headers=headers)

    # proceed only if the status code is 200
    print('The status code is {}'.format(req.status_code))

    parsed_data = json.loads(req.text)
    print(json.dumps(parsed_data, indent=4))
    return;


