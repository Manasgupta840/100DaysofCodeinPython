MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 10,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 20,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 25,
    }
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 200,
}

cost = {
    "earning": 0
}
from time import sleep

def report():
    print(
        f"Water  | {resources['water']}ml\nMilk   | {resources['milk']}ml\nCoffee | {resources['coffee']}g\nMoney  | ₹{cost['earning']}")


def checking(coffee_type):
    if resources["water"] < MENU[coffee_type]['ingredients']["water"]:
        print("Sorry there is not enough water.")
        return False
    if resources["milk"] < MENU[coffee_type]['ingredients']["milk"]:
        print("Sorry there is not enough milk.")
        return False
    if resources["coffee"] < MENU[coffee_type]['ingredients']["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True


def money_collection(coffee_type):
    one = float(input("No. of '1' Rs coin: "))
    two = float(input("No. of '2' Rs coin: "))
    five = float(input("No. of '5' Rs coin: "))
    ten = float(input("No. of '10' Rs coin: "))
    total = (one + (2 * two) + (five * 5) + (ten * 10))
    if MENU[coffee_type]["cost"] <= total:
        cost["earning"] += MENU[coffee_type]["cost"]
        resources["milk"] = resources["milk"] - MENU[coffee_type]['ingredients']["milk"]
        resources["water"] = resources["water"] - MENU[coffee_type]['ingredients']["water"]
        resources["coffee"] = resources["coffee"] - MENU[coffee_type]['ingredients']["coffee"]
        return total - MENU[coffee_type]["cost"]
    return -1


def service(coffee_type):
    if checking(coffee_type):
        return_money = money_collection(coffee_type)
        if return_money == -1:
            print("“Sorry that's not enough money. Money refunded.”")
            return True
        elif return_money != 0:
            print(f"“Here is ₹{return_money} dollars in change.”\nHere is your {coffee_type}. Enjoy!.")
            return True
        else:
            print(f"Here is your {coffee_type}. Enjoy!.")
            return True
    else:
        return False


off = True


while off:
    print(" _________________")
    print("|   Our Prices    |\n ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n| espresso  | ₹10 |\n| latte     | ₹20 |\n| cappuccino| ₹25 |")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == 'report':
        report()
    elif coffee == 'espresso' or coffee == 'latte' or coffee == 'cappuccino':
        off = service(coffee)
    else:
        print("Please choose the valid option!! ")
