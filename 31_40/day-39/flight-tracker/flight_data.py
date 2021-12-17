from dateutil import parser
import json


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, file_path):
        self.save_file_path = file_path
        self.price = None
        self.country_from = None
        self.country_to = None
        self.duration = None
        self.seats = None
        self.departure = None
        self.arrival = None

    def struct_data(self, flight_data):
        """
        Taking the response from API and processing it for the information we need

        Returns data needed for the notification:
        country_name (destination)
        price
        seats
        """
        self.price = flight_data['price']
        self.country_from = flight_data['countryFrom']['name']
        self.country_to = flight_data['countryTo']['name']
        self.duration = flight_data['duration']['total'] / 3600
        self.seats = flight_data['availability']['seats']
        self.departure = parser.parse(flight_data['utc_departure'])
        self.arrival = parser.parse(flight_data['utc_arrival'])

        struct_dict = {
            flight_data['countryTo']['name']: {
                'price': flight_data['price'],
                'country_from': flight_data['countryFrom']['name'],
                'country_to': flight_data['countryTo']['name'],
                'duration': flight_data['duration']['total'] / 3600,
                'seats': flight_data['availability']['seats'],
                'departure': str(parser.parse(flight_data['utc_departure']).date()),
                'arrival': str(parser.parse(flight_data['utc_arrival']).date())
            }
        }

        with open(self.save_file_path, "r+") as file:
            existing_data = json.load(file)
            existing_data.update(struct_dict)
            file.seek(0)
            json.dump(existing_data, file, indent=4)

        return self.country_to, self.price, self.seats
