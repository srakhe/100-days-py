import requests

questions_response = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
question_data = questions_response.json()['results']
