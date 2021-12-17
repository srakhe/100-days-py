from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def operate():
    machine = CoffeeMaker()
    menu = Menu()
    money = MoneyMachine()

    while True:
        print('What do you want to order?')
        choice = input(f'Choose your drink: {menu.get_items()}\n')

        if choice == 'off':
            return
        elif choice == 'report':
            machine.report()
            money.report()
        else:
            menu_item = menu.find_drink(choice)
            if menu_item:
                if machine.is_resource_sufficient(menu_item):
                    if money.make_payment(menu_item.cost):
                        machine.make_coffee(menu_item)


operate()
