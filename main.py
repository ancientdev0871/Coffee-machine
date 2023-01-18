from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
menu = Menu()

turn_on = True
while turn_on:
  options = menu.get_items()
  choice = input(f"What would you like to get {options}?")
  if choice == "off":
    turn_on = False
  elif choice == "report":
    my_coffee_maker.report()
    my_money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
      my_coffee_maker.make_coffee(drink)
      

