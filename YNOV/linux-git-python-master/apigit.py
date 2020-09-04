import requests
import json

def query_github():
    url = "https://api.github.com/repositories"
    reponse = requests.get(url)
    data = reponse.json()
    for dict in data:
        print(dict["name"])
        print(dict["description"])

def read_from_local_data():
    path = './repositories.json'
    file = open(path)
    content = file.read()
    file.close()
    return json.loads(content)
