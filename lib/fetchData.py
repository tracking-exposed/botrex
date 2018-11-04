# just for test purposes, needs caching.
import requests

def getBasic():
    data = requests.get("https://facebook.tracking.exposed/api/v1/stats/basic/1").json()
    return data
