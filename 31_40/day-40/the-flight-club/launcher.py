from sheets_handler import SheetsHandler
from flight_search import FlightSearch
from email_notifier import EmailNotifier
from users_handler import UsersHandler


def dealer():
    # TODO: Get data of the cities to track ticket prices for
    # This needs a sheets_handler class
    print('Welcome! Looking for routes to look for their flight deals....')
    sheets_handler_obj = SheetsHandler()
    from_cities, to_cities, prices_to_compare = sheets_handler_obj.get_cities()
    print(f'Found {len(from_cities)} routes')

    # TODO: Get the ticket prices for these cities
    # This needs a flight_search class
    print('Looking for deals now....')
    flight_search_obj = FlightSearch()
    from_cities_deals, to_cities_deals, deal_prices, deal_dates = flight_search_obj.get_prices(from_cities, to_cities,
                                                                                               prices_to_compare)
    print(f'Found deals {len(from_cities_deals)} routes')

    # TODO: If ticket price cheaper than expected, send emails!
    # This needs a mailer class
    print('Notifying users of the deal(s) (if any)....')
    email_notifier_obj = EmailNotifier()
    user_names, user_emails = sheets_handler_obj.get_users()
    for each_from_city, each_to_city, deal_price, deal_date in zip(from_cities_deals, to_cities_deals, deal_prices,
                                                                   deal_dates):
        for user_name, user_email in zip(user_names, user_emails):
            email_notifier_obj.send_emails(user_name, user_email, each_from_city, each_to_city, deal_price, deal_date)
    print('Notified!')


def add_users():
    # TODO: Add new users to email list (Just add to google sheet)
    # This needs a user class
    users_handler_obj = UsersHandler()
    cont = input('Add a new user? (Y/n)')
    while cont == 'Y' or cont == 'y':
        users_handler_obj.add_user()
        cont = input('Add another user? (Y/n)')


dealer()
add_users()
