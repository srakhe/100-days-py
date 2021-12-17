def greet():
    print('Hello')
    print('World')
    print('This is a function')


greet()


def greet_name(name):
    print(f'Hello {name}')


greet_name('Sam')
greet_name(input('What\'s your name?\n'))


def greet_multi(name, location):
    print(f'Hello {name}')
    print(f'How is the weather in {location}?')


greet_multi(input('What\'s your name?\n'), input('Where are you from?\n'))
