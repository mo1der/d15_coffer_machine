# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "milk": 0,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# profit = 0
#
# def report():
#     print(f"Water: {resources['water']}ml")
#     print(f"Milk: {resources['milk']}ml")
#     print(f"Coffee: {resources['coffee']}g")
#     print(f"Money: {profit}$")
#
# def check_resources(coffe_type):
#     resources_ok = True
#     if int(MENU[coffe_type]["ingredients"]["water"]) > int(resources["water"]):
#         print('Sorry there is not enough water.')
#         resources_ok = False
#     if int(MENU[coffe_type]["ingredients"]["milk"]) > int(resources["milk"]):
#         print('Sorry there is not enough milk.')
#         resources_ok = False
#     if int(MENU[coffe_type]["ingredients"]["coffee"]) > int(resources["coffee"]):
#         print('Sorry there is not enough coffee.')
#         resources_ok = False
#     if resources_ok == True:
#         print("zasoby ok")
#         return True
#     else:
#         print("zasoby nok")
#         return False
#
# def process_coints():
#     inserted_amount = 0
#     inserted_quarters = int(input(f'How many $0.25 quarters?: '))
#     inserted_dimes = int(input(f'How many $0,10 dimes?: '))
#     inserted_nickels = int(input(f'How many $0,05 nickles?: '))
#     inserted_pennies = int(input(f'How many $0,01 pennies?: '))
#     inserted_amount = inserted_quarters * 0.25 + inserted_dimes * 0.10 + inserted_nickels * 0.05 + inserted_pennies * 0.01
#     return inserted_amount
#
# def update_resources(coffe_type):
#     resources["water"] -= MENU[coffe_type]["ingredients"]["water"]
#     resources["milk"] -= MENU[coffe_type]["ingredients"]["milk"]
#     resources["coffee"] -= MENU[coffe_type]["ingredients"]["coffee"]
#
# machine_on = True
# while machine_on == True:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         machine_on = False
#     elif choice == "report":
#         report()
#     elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
#         if check_resources(choice) == True:
#             print(f'{choice} cost is ${int(MENU[choice]["cost"])}. Insert coins.')
#             inserted_amount = 0
#             inserted_amount = process_coints()
#             if inserted_amount < int(MENU[choice]["cost"]):
#                 print(f"Sorry that's not enough money. Money ${inserted_amount}refunded.")
#             else:
#                 if inserted_amount > int(MENU[choice]["cost"]):
#                     money_back = round(inserted_amount - int(MENU[choice]["cost"]),2)
#                     print(f'Payment ok. You inserted too much money. ${money_back} refunded')
#                 else:
#                     print(f'Payment ok.')
#                 print(f'Making coffee ...... ')
#                 print(f"Here is your {choice}. Enjoy!\n")
#                 update_resources(choice)
#                 profit += int(MENU[choice]["cost"])
#         else:
#             print("Brak składników.")
#     else:
#         print("Unknown command, try again.")


from menu import Menu, MenuItem
from coffee_maker import CaffeMaker
from money_machine import MoneyMachine

mo1der_coffee_maker = CaffeMaker()
mo1der_money_machine = MoneyMachine()
mo1der_menu = Menu()

machine_on = True
while machine_on:
    choice = input(f"What would you like? {mo1der_menu.get_items()}: ")
    if choice == "report":
        mo1der_coffee_maker.report()
        mo1der_money_machine.report()
    elif choice == "off":
        machine_on = False
        break
    elif choice in mo1der_menu.get_items():
        drink = mo1der_menu.find_drink(choice)
        print(f"Your {drink.name} cost is {drink.cost}.")
        if mo1der_coffee_maker.is_resource_sufficient(drink) == True and mo1der_money_machine.make_payment(drink.cost) == True:
            mo1der_coffee_maker.make_coffee(drink)


