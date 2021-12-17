from config_handler import ConfigHandler
import requests


class SheetsHandler:

    def __init__(self):
        self.config_data = ConfigHandler()
        self.users_url = None
        self.flights_url = None
        self.sheet_auth = None
        self.users_url, self.flights_url, self.sheet_auth = self.config_data.get_sheets_data()

    def get_cities(self):
        """
        Method to get a list of cities to track the prices for.
        Returns:
            from_cities: A list of departure cities
            to_cities: A list of destination cities
            prices_to_compare: A list of prices for these routes to compare to
        """
        header = {
            'Authorization': self.sheet_auth
        }
        flights_response = requests.get(self.flights_url, headers=header)
        flights = flights_response.json()['flights']
        from_cities = []
        to_cities = []
        prices_to_compare = []
        for each_entry in flights:
            from_cities.append(each_entry['from'])
            to_cities.append(each_entry['to'])
            prices_to_compare.append(each_entry['comparePrice'])
        return from_cities, to_cities, prices_to_compare

    def get_users(self):
        """
        This method returns a list of user's names and their emails, that have signed up to be notified
        """
        header = {
            'Authorization': self.sheet_auth
        }
        users_response = requests.get(self.users_url, headers=header)
        users = users_response.json()['users']
        user_names = []
        user_emails = []
        for each_entry in users:
            user_names.append(each_entry['name'])
            user_emails.append(each_entry['email'])
        return user_names, user_emails

    def add_user(self, name, email):
        """
        This method will add a new user to the list of users in the google sheet.
        """
        header = {
            'Authorization': self.sheet_auth
        }
        data = {
            'user': {
                'name': str(name),
                'email': str(email)
            }
        }
        return requests.post(self.users_url, json=data, headers=header)
