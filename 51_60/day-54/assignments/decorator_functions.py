import time


# def add(x, y):
#     return x + y
#
#
# def subtract(x, y):
#     return x - y
#
#
# def multiply(x, y):
#     return x * y
#
#
# def divide(x, y):
#     return x // y
#
#
# def calc(operator, x, y):
#     return operator(x, y)
#
#
# print(calc(add, 2, 3))
#
#
# def outer_funct():
#     print('Hello')
#
#     def inner_funct():
#         print('Im inside!')
#
#     inner_funct()
#     return inner_funct
#
#
# get_funct = outer_funct()
# get_funct()

def delay_decorator(function):
    time.sleep(2)

    def wrapper():
        function()

    return wrapper


# def say_hello():
#     time.sleep(5)
#     print('Hello after 5 seconds!')

# THIS IS THE SAME AS
@delay_decorator
def say_hello():
    print('Hello after 2 seconds')


def say_hello_instant():
    print('Hello isntant')


# THIS
decorated_funct = delay_decorator(say_hello_instant)
decorated_funct()

# A very very impo note:
# A DECORATOR FUNCTION is a function that consists of a wrapper function
# This wrapper function can control the calling of the function passed to the dec func as an argument
# So overall, the dec funct adds some funct AND controls the calling of the given function!

# Syntax:
# Wrapper funct() inside dec funct() the wrapper calls the funct that is passed as an argument to the dec funct()
# The wrapper funct is then returned at the end

say_hello()
