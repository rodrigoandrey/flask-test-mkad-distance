import os
import requests
from dotenv import load_dotenv
from math import sin, cos, sqrt, atan2, radians

load_dotenv()

YOUR_ACCESS_KEY = os.environ.get('YOUR_ACCESS_KEY')


# function to obtain the geocoding
def get_location(address, city):
    url = f'http://api.positionstack.com/v1/forward?access_key={YOUR_ACCESS_KEY}&query={address},{city}'
    r = requests.get(url)
    rjson = r.json()
   # print(rjson)
    geo_location = {
        'latitude': rjson["data"][0]["latitude"],
        'longitude': rjson["data"][0]["longitude"]
    }

    return geo_location


# function to obtain the distance
def get_distance(geo_location):
    # Approximate radius of earth in km
    EARTH_RADIUS = 6373.0

    # MOSCOW CENTER 55.75162795716288, 37.62329094071195
    MC_LAT = radians(55.75162795716288)
    MC_LON = radians(37.62329094071195)
    MKAD_RADIUS = 17

    # Target Location
    TARGET_LAT = radians(geo_location.get('latitude'))
    TARGET_LON = radians(geo_location.get('longitude'))

    dlon = TARGET_LON - MC_LON
    dlat = TARGET_LAT - MC_LAT

    a = sin(dlat / 2)**2 + cos(MC_LAT) * cos(TARGET_LAT) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = (EARTH_RADIUS * c) - MKAD_RADIUS

    if distance <= MKAD_RADIUS:
        distance = 0
        return distance
    else:
        return distance
