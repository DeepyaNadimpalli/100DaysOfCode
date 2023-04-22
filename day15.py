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


def check_resources(coffee):
    """This function is used to check whether the ingredients required for the selected coffee are present in resources
    or not"""
    for key, val in (MENU[coffee]["ingredients"]).items():
        if resources[key] < val:
            global not_enough
            not_enough = key
            return False
    return True


def process_coins(quarters, dimes, nickles, pennies):
    """This function converts all the coins into dollars"""
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


def make_coffee(coffee):
    """This function would remove the ingredients needed to make the selected coffee"""
    for key, val in MENU[coffee]["ingredients"].items():
        resources[key] -= val


turn_off = False
profit = 0
while not turn_off:
    user_wants = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_wants == "off":
        turn_off = True
    elif user_wants == "report":
        for key1, val1 in resources.items():
            if key1 == "coffee":
                print(f"{key1}: {val1}g")
            else:
                print(f"{key1}: {val1}ml")
        print(f"Money: ${profit}")
    elif user_wants in ["espresso", "latte", "cappuccino"]:
        not_enough = ""
        if check_resources(user_wants):
            print(f"Please insert coins.")
            quarters = int(input("how many quarters?:"))
            dimes = int(input("how many dimes?:"))
            nickles = int(input("how many nickels?:"))
            pennies = int(input("how many pennies?:"))
            money_received = process_coins(quarters, dimes, nickles, pennies)
            if money_received > MENU[user_wants]["cost"]:
                change = round(money_received - MENU[user_wants]["cost"], 2)
                print(f"Here is ${change} dollars in change.")
                profit += MENU[user_wants]["cost"]
                make_coffee(user_wants)
                print(f"Here is your {user_wants}. Enjoy!")
            elif money_received == MENU[user_wants]["cost"]:
                # add_profit(money_received)
                profit += MENU[user_wants]["cost"]
                make_coffee(user_wants)
                print(f"Here is your {user_wants}. Enjoy!")
            else:
                print(f"Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {not_enough}.")
    else:
        print(f"You entered wrong choice")
