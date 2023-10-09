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
Profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def process_coin():
    print("please insert coin")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickless?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global Profit
        Profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕.enjoy")



is_on = True
while True:
    Choice = input("What would you like? (espresso/latte/cappuccino): ")
    if Choice == "off":
        is_on = False
    elif Choice == "report":
        print(f"Water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"Money: ${Profit}")
    else:
        drink = MENU[Choice]
        if is_resource_sufficient(drink["ingredients"]):
           payment = process_coin()
           if is_transaction_successful(payment, drink["cost"]):
               make_coffee(Choice, drink["ingredients"])



