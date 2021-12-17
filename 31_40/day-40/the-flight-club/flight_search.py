from config_handler import ConfigHandler
from datetime import datetime
from datetime import timedelta
from dateutil import parser
import requests


class FlightSearch:

    def __init__(self):
        self.config_data = ConfigHandler()
        self.flight_search_api_key = None
        self.flight_search_url = None
        self.flight_search_url, self.flight_search_api_key = self.config_data.get_flight_search_data()

    def get_prices(self, from_cities, to_cities, prices_to_compare):
        """
        Returns lists of routes that have flight deals for those routes
        """
        from_cities_deals = []
        to_cities_deals = []
        deal_prices = []
        deal_dates = []
        for each_from_city, each_to_city, price_to in zip(from_cities, to_cities, prices_to_compare):
            tomorrow = (datetime.today() + timedelta(days=1)).date().strftime('%d/%m/%Y')
            limit_date = (datetime.today() + timedelta(days=(6 * 30))).date().strftime('%d/%m/%Y')

            headers = {
                'apikey': self.flight_search_api_key
            }

            print(f'Looking for route: {each_from_city} to {each_to_city}')

            params = {
                'fly_from': each_from_city,
                'fly_to': each_to_city,
                'date_from': str(tomorrow),
                'date_to': str(limit_date),
                'curr': 'INR',
                'price_to': str(price_to)
            }

            response = requests.get(url=self.flight_search_url, params=params, headers=headers)
            flight_data = response.json()['data']

            for item in flight_data:
                if item['availability']['seats']:
                    from_cities_deals.append(item['cityFrom'])
                    to_cities_deals.append(item['cityTo'])
                    deal_prices.append(item['price'])
                    deal_dates.append(str(parser.parse(item['utc_departure']).date()))
                    break
        return from_cities_deals, to_cities_deals, deal_prices, deal_dates
