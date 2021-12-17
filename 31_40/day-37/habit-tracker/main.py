import requests
from datetime import datetime
import os

TOKEN = os.environ['MY_TOKEN']
USER = os.environ['MY_USER']
GRAPH_ID = 'daily-courses'

api_users_endpoint = 'https://pixe.la/v1/users'
api_graph_endpoint = f'{api_users_endpoint}/{USER}/graphs'
api_graph_name_endpoint = f'{api_users_endpoint}/{USER}/graphs/{GRAPH_ID}'


def create_user():
    user_params = {'token': TOKEN,
                   'username': USER,
                   'agreeTermsOfService': 'yes',
                   'notMinor': 'yes'}
    response = requests.post(url=api_users_endpoint, json=user_params)
    print(response.text)


def create_graph_def():
    graph_params = {'id': GRAPH_ID,
                    'name': 'daily-courses-tracker',
                    'unit': 'commit',
                    'type': 'int',
                    'color': 'ichou'}
    graph_headers = {'X-USER-TOKEN': TOKEN}
    response = requests.post(url=api_graph_endpoint, json=graph_params, headers=graph_headers)
    print(response.text)


def add_graph_value(quantity):
    graph_params = {'date': str(datetime.today().date().strftime('%Y%m%d')),
                    'quantity': str(quantity)}
    graph_headers = {'X-USER-TOKEN': TOKEN}
    response = requests.post(url=api_graph_name_endpoint, json=graph_params, headers=graph_headers)
    print(
        f'For date: {datetime.today().date().strftime("%Y%m%d")}, you pushed: {quantity}, message was: {response.text}')


create_user()
create_graph_def()
add_graph_value(10)
