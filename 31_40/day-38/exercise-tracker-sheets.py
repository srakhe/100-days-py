import requests
from datetime import datetime
import os

NLP_APP_ID = os.environ['NLP_APP_ID']
NLP_API_KEY = os.environ['NLP_API_KEY']
EXERCISE_ENDPOINT = os.environ['EXERCISE_ENDPOINT']
SHEETS_TOKEN = os.environ['SHEETS_TOKEN']


def get_exercise_data(query):
    headers = {
        'x-app-id': NLP_APP_ID,
        'x-app-key': NLP_API_KEY,
        'x-remote-user-id': '0'
    }

    params = {
        'query': query
    }

    response = requests.post(url=EXERCISE_ENDPOINT, json=params, headers=headers)
    response = response.json()

    exercises = response['exercises']
    for each_exercise in exercises:
        exercise_name = str(each_exercise['name']).title()
        exercise_duration = each_exercise['duration_min']
        exercise_cals = each_exercise['nf_calories']
        send_to_sheet(exercise_name, exercise_duration, exercise_cals)


def send_to_sheet(exercise, duration, calories):
    headers = {
        'Authorization': SHEETS_TOKEN
    }

    today = datetime.today().date().strftime('%d/%m/%Y')
    time_now = datetime.now().time().strftime('%H:%M:%S')

    data_to_send = {
        'workout': {
            'date': today,
            'time': time_now,
            'exercise': exercise,
            'duration': duration,
            'calories': calories
        }
    }

    response = requests.post(url='https://api.sheety.co/3df8ea1b6e60c598841fd7589d4c5e6f/myWorkouts/workouts',
                             json=data_to_send, headers=headers)
    print(response.json())


exercise_done = input('What did you do today?\n')
get_exercise_data(exercise_done)
