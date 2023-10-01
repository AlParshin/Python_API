
import requests as requests
import yaml

with open('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)


def get(token: str):
    response = requests.get(conf['url_post'],
                            headers={'X-Auth-Token': token},
                            params={'owner': 'notMe'})
    print(response.json)
    return response.json()


def create_post(token: str):
    requests.post(conf['url_post'],
                  headers={'X-Auth-Token': token},
                  params={'title': 'title12345', 'description': 'desc45678', 'content': 'cont56789'})


def get_by_description(token: str):
    response = requests.get(conf['url_post'],
                            headers={'X-Auth-Token': token},
                            params={'description': 'desc45678'})
    print(response.json)
    return response.json()
