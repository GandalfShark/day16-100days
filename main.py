"""
Pretend coffee machine round 2 - OOP version
using pre-constructed classes and methods from
100 days of python day 16. by Dr. Angela Yu
"""
print("""
_____________________________
WELCOME to PRETEND COFFEE 2.0
-----------------------------
""")

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
on = True
# create drinks here
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while on:
    # ask for type of coffee
    coffee_choice = input(f'What would you like? {menu.get_items()} ?')
    while coffee_choice not in ['report', 'off', 'latte', 'espresso', 'cappuccino']:
        coffee_choice = input(f'Please enter a valid choice\n{menu.get_items()}? ')
    if coffee_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    # provide a way to turn off machine
    elif coffee_choice == 'off':
        print('shutting down')
        on = False
    else:
        drink = menu.find_drink(coffee_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

