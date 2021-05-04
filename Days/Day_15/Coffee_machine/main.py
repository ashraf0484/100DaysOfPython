from data import *
from os import system

system("clear")


def resources_updater(drink):
    """Updates the level of resources_left once a drink is made"""
    # if drink != "espresso":
    #     resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    # resources["water"] -= MENU[drink]["ingredients"]["water"]
    # resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]

    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]


def report_printer(resources_left):
    """Prints the report for the remaining resources"""
    print(f"Water: {resources_left['water']}ml")
    print(f"Milk: {resources_left['milk']}ml")
    print(f"Coffee: {resources_left['coffee']}g")
    print(f"Money: ${money}")


def resource_checker(drink):
    """Checks and return boolean values if there's sufficient amount of resources available or not"""
    # if drink != "espresso":
    #     if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
    #         print("Sorry, there is no enough milk")
    #         return False
    # if resources["water"] < MENU[drink]["ingredients"]["water"]:
    #     print("Sorry, there is no enough water")
    #     return False
    # elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
    #     print("Sorry, there is no enough coffee")
    #     return False
    # else:
    #     return True

    for item in resources:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry, there is no enough {item}")
            return False
        else:
            return True


def coin_calculator(drink, total_money):
    """Calculates the coins given by the customer."""
    resources_updater(drink)
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = ((quarters * 25) + (dimes * 10) + (nickles * 5) + (pennies * 1)) / 100
    rate = MENU[drink]["cost"]
    if total < rate:
        print("Insufficient coins")
    else:
        change = round(total - rate, 2)
        print(f"Here is ${change} in change.")
        total_money += rate
        return total_money


money = 0
machine_on = True

while machine_on:
    selection = input("What would you like? (espresso/latte/cappuccino)").lower()
    if selection == "off":
        machine_on = False
    elif selection == "report":
        report_printer(resources)
    elif selection in MENU:
        if resource_checker(selection):
            print("Please insert coins.")
            money += coin_calculator(selection, money)
            print(f"Here is your {selection} ☕️ Enjoy!")
        else:
            print("Please collect your coins.")
    else:
        print("Enter a valid input.")
