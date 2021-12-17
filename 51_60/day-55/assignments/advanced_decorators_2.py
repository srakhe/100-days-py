def logging_detector(funct):
    def wrapper(*args, **kwargs):
        print(f'The function called was {funct.__name__}')
        print('Arguments passed:')
        for arg in args:
            print(arg)
        print(funct(*args))

    return wrapper


@logging_detector
def homer(name, day, rating):
    return 'HOMER'


@logging_detector
def tempo(song, singer, bpm):
    return 'Rock it up!'


homer('sam', 'bad', 'worst')
tempo('Yo', 'Bonny', 125)
