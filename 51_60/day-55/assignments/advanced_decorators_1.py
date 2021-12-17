class User:

    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def login_detector(funct):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            funct(args[0])

    return wrapper


@login_detector
def create_blog(user):
    print(f'Blog created for {user.name}')


my_user = User('Sam')
my_user.is_logged_in = True
create_blog(my_user)
