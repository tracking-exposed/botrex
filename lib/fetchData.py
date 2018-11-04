import requests
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=1, ttl=600) # maxsize is 1 because we only fetch one element. time to live is 10 mins.

@cached(cache)
def getBasic():
    url = "https://facebook.tracking.exposed/api/v1/stats/basic/1"
    print("Accessing", url)
    data = requests.get(url).json()
    return data
