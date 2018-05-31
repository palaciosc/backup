import requests
import pprint
import json

url = "https://api.xplenty.com/erea/api/clusters/search?limit=100"

querystring = {
        "q":"status:terminated, name:KAD",
        "sort":"created",
        "direction":"desc"
    }

headers = {
    'Accept': "application/vnd.xplenty+json; version=2",
    'Content-Type': "application/json",
    'Authorization': "Basic Q1paeFlWVjhBaWFQcWc1akRzSDc6",
    'Cache-Control': "no-cache",
    'Postman-Token': "08d8c684-7c2d-4cd6-a216-aa329d364541"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

with open('clusters.json', 'w') as outfile:
    json.dump(response.json(), outfile)

pprint.pprint(len(response.json()))
#pprint.pprint(response.json())