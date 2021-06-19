import requests
import json


def reqSumDate(weight):
    api_url = "https://pokeapi.co/api/v2/pokemon/" + weight

    status_codes = [400, 401, 403, 404, 405, 415, 429, 500, 502, 503, 504]
    if requests.get(api_url).status_code in status_codes:
        print("HATA Kod: " + str(requests.get(api_url).status_code))

    dataText = requests.get(api_url).text
    dataJson = json.loads(dataText)
    weight = dataJson["weight"]

    return str(weight)
