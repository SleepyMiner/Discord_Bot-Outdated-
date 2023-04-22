import requests
import json


def get_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    json_data = json.loads(response.text)
    joke = json_data["value"]
    return (joke)