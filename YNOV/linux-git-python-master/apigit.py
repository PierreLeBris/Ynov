import requests
import json
import sys

def query_github():
    url = "https://api.github.com/repositories"
    reponse = requests.get(url)
    data = reponse.json()
    for dict in data:
        print(dict["name"])
        print(dict["description"])
        
def read_from_local_data():
    path = '/home/pierre/Bureau/YNOV/linux-git-python-master/repositories.json'
    file = open(path)
    content = file.read()
    file.close()
    return json.loads(content)

sys.stdout = open('test.txt','wt')
print(query_github())