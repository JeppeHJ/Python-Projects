from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()
#my_items = MenuItem()



is_on = True
while is_on:
    options = my_menu.get_items()
    choice = input(f"What do you want? {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_money_machine.report()
        my_coffee_maker.report()
    else:
        drink = my_menu.find_drink(choice)
        if drink:
            if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)




