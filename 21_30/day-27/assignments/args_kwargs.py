def a_function(a, b=10):
    return a + b


print(a_function(10))


# Use of *args: (Can use anything but common is *args)
def another_function(*args):
    print(args)
    print(type(args))
    # (14, 5, 6, 7, 8)
    # <class 'tuple'>
    sum = 0
    for number in args:
        sum += number
    return sum


print(another_function(14, 5, 6, 7, 8))


# Use of kwargs:
def keywords_function(**kwargs):
    print(kwargs)  # This is a dict
    # return kwargs['a'] + kwargs['b']
    # This was one way but get() is better
    # As if the key doesnt exist, it wont crash
    # It only returns None
    # Use this instead
    return kwargs.get('a') + kwargs.get('b')


print(keywords_function(a=21, b=22))
