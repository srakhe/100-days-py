import requests
from datetime import datetime
from datetime import timedelta


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, api_key, url):
        self.flight_search_api_key = api_key
        self.flight_search_url = url

    def search_flights(self, from_city, to_city, currency, months):
        """ Returns a dict with data of the cheapest flight available """
        tomorrow = (datetime.today() + timedelta(days=1)).date().strftime('%d/%m/%Y')
        limit_date = (datetime.today() + timedelta(days=(months * 30))).date().strftime('%d/%m/%Y')

        headers = {
            'apikey': self.flight_search_api_key
        }

        params = {
            'fly_from': from_city,
            'fly_to': to_city,
            'date_from': tomorrow,
            'date_to': limit_date,
            'curr': currency
        }

        response = requests.get(url=self.flight_search_url, params=params, headers=headers)
        flight_data = response.json()['data']

        for item in flight_data:
            if item['availability']['seats']:
                return item
