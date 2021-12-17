MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MONEY_IN_MACHINE = 0


# TODO 1: What would you like (espresso/latte/cappuccino)
# TODO 2: "off" prompt
# TODO 3: Print report
# TODO 4: Check if sufficient resources
# TODO 5: Process coins
# TODO 6: Check transaction
# TODO 7: Make coffee

def report():
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: ${MONEY_IN_MACHINE}')


def check_resources(coffee):
    need_water = MENU[coffee]['ingredients']['water']
    need_milk = MENU[coffee]['ingredients']['milk'] if not coffee == 'espresso' else 0
    need_coffee = MENU[coffee]['ingredients']['coffee']
    have_water = resources['water']
    have_milk = resources['milk']
    have_coffee = resources['coffee']
    can_make = True
    if need_water > have_water:
        can_make = False
        print('Not enough water!')
    elif need_milk > have_milk:
        can_make = False
        print('Not enough milk')
    elif need_coffee > have_coffee:
        can_make = False
        print('Not enough coffee')
    return can_make


def process_coins():
    penny = int(input('How many pennies?'))
    nickel = int(input('How many nickles?'))
    dime = int(input('How many dimes?'))
    quart = int(input('How many quaters?'))
    total = (0.01 * penny) + (0.05 * nickel) + (0.10 * dime) + (0.25 * quart)
    print(f'Amount received= ${total}')
    return total


def money_calc(coffee, money_received):
    money_needed = MENU[coffee]['cost']
    if money_needed <= money_received:
        return money_received - money_needed
    else:
        print(f'Sorry! That\'s not enough money for the {coffee}')
        return False


def use_resources(coffee):
    need_water = MENU[coffee]['ingredients']['water']
    need_milk = MENU[coffee]['ingredients']['milk'] if not coffee == 'espresso' else 0
    need_coffee = MENU[coffee]['ingredients']['coffee']
    resources["water"] -= need_water
    resources["milk"] -= need_milk
    resources['coffee'] -= need_coffee


def make_coffee(coffee):
    global MONEY_IN_MACHINE
    if check_resources(coffee):
        money = process_coins()
        money_diff = money_calc(coffee, money)
        if money_diff:
            print(f'Change tendered= ${money_diff}')
            MONEY_IN_MACHINE = MONEY_IN_MACHINE + (money - money_diff)
            use_resources(coffee)
            print(f'Here\'s your {coffee}☕, enjoy!')


def operate():
    while True:
        choice = input('What would you like? (espresso/latte/cappuccino) \n').lower()
        if choice == 'off':
            return
        elif choice == 'report':
            report()
        elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            make_coffee(choice)


operate()
