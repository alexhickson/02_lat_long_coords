# Built with python 3, dependencies installed with pip
# library to generate images - Pillow 
# HTTP library - https://docs.python-requests.org/en/latest/
import requests

# subscription key
subscription_key = "38bc9b402fef4ac2ab7091a1f35d5a3b"


# Create a function that requires two parameters:
# 1. Subscription Key — specific to the resource
# 2. Query — your own web search string
def bing_web_search(subscription_key, query):
    # set parameters
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {
        "q": query,
        "textDecorations": True,
        "textFormat": "HTML"}
    # get response
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

# call API
home_address = '43 Hamilton Road, Walthamstow'
search_results = bing_web_search(subscription_key, query= home_address + ' latitude longitude')

url = search_results['webPages']['value'][0]['url']

# zpid = [x for x in url.split('/') if 'zpid' in x][0].split('_')[0]
print(url)