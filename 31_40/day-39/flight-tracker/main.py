from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import os

SHEET_AUTH = os.environ['SHEET_AUTH']
SHEET_URL = os.environ['SHEET_URL']
FLIGHT_SEARCH_URL = os.environ['FLIGHT_SEARCH_URL']
FLIGHT_SEARCH_API_KEY = os.environ['FLIGHT_SEARCH_API_KEY']
DATA_FILE = 'data/flight_search_data.json'
SMS_API_KEY = os.environ['SMS_API_KEY']
TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_AUTH = os.environ['TWILIO_AUTH']

# This file will need to use the DataManager,FlightSearch, FlightData
# and NotificationManager classes to achieve the program requirements.

# TODO: Use data_manager.py to fetch rows from sheet and find out what cities to get flight prices for.
data_manager_obj = DataManager(SHEET_AUTH, SHEET_URL)
list_search = data_manager_obj.get_sheet_data()

# TODO: Use this data to search flights from flight_search.py for given cities for the next 4 months from tomorrow
flight_search_obj = FlightSearch(FLIGHT_SEARCH_API_KEY, FLIGHT_SEARCH_URL)
# TODO: Use flight_data.py to structure data fetched from flight API
flight_data_obj = FlightData(file_path=DATA_FILE)
# TODO: Use notification_manager.py to send SMS notification if flights are found at a price cheaper than specified
notification_manager_obj = NotificationManager(TWILIO_SID, TWILIO_AUTH)

for each_city in list_search:
    from_city = each_city['iataFrom']
    to_city = each_city['iataTo']
    flight_search_data = flight_search_obj.search_flights(from_city=from_city, to_city=to_city, currency='INR',
                                                          months=4)
    if flight_search_data:
        # Structure data and generate a notification
        country, price, seats = flight_data_obj.struct_data(flight_search_data)
        notification_manager_obj.notify_sms(country, price, seats)
