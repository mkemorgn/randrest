import os
import requests
import json
import getRestaurant
from pprint import pprint
from dotenv import load_dotenv

#loads env variables
load_dotenv()

# makes request to yelp, parses json then prints the response
getRestaurant.get_restaurant()

