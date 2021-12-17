from configparser import ConfigParser

CONFIG_FILE = 'data/config.ini'


class ConfigHandler:

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(CONFIG_FILE)

    def get_sheets_data(self):
        """
        Returns:
            Sheets url for users page
            Sheets url for the flights page
            Sheets auth token
        """
        sheets_data = self.config['SHEETS DATA']
        return str(sheets_data['users_url']), str(sheets_data['flight_url']), str(sheets_data['auth'])

    def get_flight_search_data(self):
        """
        Returns:
            Flight search url
            Flight search api key
        """
        flight_search_data = self.config['FLIGHT SEARCH']
        return str(flight_search_data['flight_search_url']), str(flight_search_data['flight_search_api_key'])

    def get_email_data(self):
        """
        Returns:
            Gmail smtp server
            Gmail smtp port number
            Senders email address
            Senders email password
        """
        gmail_data = self.config['GMAIL DATA']
        return str(gmail_data['smtp_address']), int(gmail_data['smtp_port']), str(gmail_data['sender']), str(
            gmail_data['sender_pass'])
