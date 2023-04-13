# Built with python 3, dependencies installed with pip
# HTTP library - https://docs.python-requests.org/en/latest/
# panda used to load csv files to data frames
import pandas as pd

# requests used to generate url request
import requests

# json used to parse json files 
import json

# read in csv containing the name of the address, the postal code and city
df = pd.read_csv ('addresses.csv')

# subscription key from https://www.bingmapsportal.com/Application#
subscription_key = "Ai2m2VKFl6iFKhB8p_2ZFl7JlBzX5LOHU2wq4tYgKTWPZ0mCcPWSI-Kf7znUWxFZ"

for i in range(df.shape[0]):
    # take each cell from the row being iterated
    addressLine = df.at[i, 'Address']
    postalCode = df.at[i, 'Postal Code']
    city = df.at[i, 'City']
    
    # combine search URL with city, postal code, address line & BING Maps API subscription key
    # search url example e.g http://dev.virtualearth.net/REST/v1/Locations?locality=London&postalCode=E176EH&key
    search_url = "http://dev.virtualearth.net/REST/v1/Locations?locality=" + city + "&postalCode=" + postalCode + "&addressLine=" + addressLine + "&key=" + subscription_key
    print(search_url)
    
    # execute the URL search & store co-ordinates by parsing the JSON reponse
    response = requests.get(search_url)
    location_dict = response.json()
    coordinates = location_dict['resourceSets'][0]['resources'][0]['point']['coordinates']
    print(coordinates)

    # # commented out option to store latitude and longitude as different values
    # latitude = coordinates[0]
    # longitude = coordinates[1]
    # print(coordinates)
    # print(longitude)
    
print("End")