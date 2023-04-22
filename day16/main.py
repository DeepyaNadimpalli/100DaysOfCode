from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu1 = Menu()
coffee_maker1 = CoffeeMaker()
money_machine1 = MoneyMachine()
turn_off = False
while not turn_off:
    order_name = input(f"What would you like? { menu1.get_items() }:")
    if order_name=="off":
        turn_off=True
    elif order_name=="report":
        coffee_maker1.report()
        money_machine1.report()
    else:
        if coffee_maker1.is_resource_sufficient(menu1.find_drink(order_name)):
            if money_machine1.make_payment((menu1.find_drink(order_name)).cost) :
                coffee_maker1.make_coffee(menu1.find_drink(order_name))

