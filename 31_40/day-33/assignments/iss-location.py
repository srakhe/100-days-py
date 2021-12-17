import json
import requests

iss_location_response = requests.get('http://api.open-notify.org/iss-now.json')
iss_location_response.raise_for_status()
print(json.loads(iss_location_response.text))
