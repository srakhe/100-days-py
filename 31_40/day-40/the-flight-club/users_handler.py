from sheets_handler import SheetsHandler


class UsersHandler:

    def __init__(self):
        self.sheets_handler_obj = SheetsHandler()

    def add_user(self):
        """
        This method will add a new user to be notified on deals!
        """
        name = input('Enter your name')
        email = input('Enter your email address (this will be used to notify you)')
        self.sheets_handler_obj.add_user(name, email)
