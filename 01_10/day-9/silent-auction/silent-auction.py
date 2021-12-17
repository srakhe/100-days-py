from art import logo

print(logo)


def insertUntil():
    bid_data = {}
    again = True
    while again:
        name = input('What\'s your name?')
        bid_price = int(input('What\'s your bid price?'))
        bid_data[name] = bid_price
        again = True if input('Do you want to continue?').lower() == 'yes' else False
        print('\n' * 50)
    return bid_data


def getMax(bid_data):
    max = 0
    max_name = ''
    for name in bid_data:
        if bid_data[name] > max:
            max_name = name
            max = bid_data[name]
    return max_name, max


bid_data = insertUntil()
name, max_bid = getMax(bid_data)
print(f'The highest bid was by {name} of ${max_bid}')
