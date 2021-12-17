import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self, auth, url):
        self.sheet_auth = auth
        self.sheet_url = url

    def get_sheet_data(self):
        """
        Returns the data fetched from the sheet:
        As of now, it returns a list of dicts.
        Each dict represents a city to search flights for.

        { 'from', 'iata_from', 'to', 'iata_to', 'lowestPrice' }
        """
        headers = {
            'Authorization': f'Bearer {self.sheet_auth}'
        }
        response = requests.get(url=self.sheet_url, headers=headers)
        response_data = response.json()['prices']
        return response_data
