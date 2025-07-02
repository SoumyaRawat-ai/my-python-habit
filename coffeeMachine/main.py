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
instructions = True
profit = 0
print(MENU["espresso"]["ingredients"]['water'])
def compare():
    if MENU[instruction]["ingredients"]['water'] > resources["water"]:
        print("Sorry there is not enough water.")
    elif MENU[instruction]["ingredients"]['water'] < resources["water"]:
        resources["water"] -= MENU[instruction]["ingredients"]["water"]
    if MENU[instruction]["ingredients"].get('milk',0) > resources.get('milk',0):
        print("Sorry there is not enough milk.")
    elif MENU[instruction]["ingredients"].get('milk', 0) < resources.get("milk", 0):
        resources['milk'] -= MENU[instruction]["ingredients"].get('milk',0)
    if MENU[instruction]["ingredients"]['coffee'] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
    elif MENU[instruction]["ingredients"]['coffee'] < resources["coffee"]:
        resources["coffee"] -= MENU[instruction]["ingredients"]["coffee"]
total = 0

def coin_management(q, d, n, p):
    quarters = 0.25
    dimes = 0.10
    nickels = 0.05
    pennies = 0.01
    total = q * quarters + d * dimes + n * nickels + p * pennies
    if total < MENU[instruction]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif total >= MENU[instruction]["cost"]:
        global profit
        profit += MENU[instruction]["cost"]
        refund = total - MENU[instruction]["cost"]
        print(f"Here is your {instruction}. Enjoy!")
        x = round(refund, 2)
        print(f"Your change: {x}")
# compare("espresso")
 # TODO: 1. Print report of all coffee machine resources 🦁🦒
machine_strat = True
while machine_strat:
    instructions = True
    while instructions:
        instruction = input("What would you like? (espresso/latte/cappuccino):").lower()
        if instruction =="report":
            print(resources)
            print(f"Profit: {profit}")
        elif instruction == "espresso" or instruction == "latte" or instruction == "cappuccino" :
            if MENU[instruction]["ingredients"]['water'] < resources["water"] and MENU[instruction]["ingredients"].get('milk', 0) < resources["milk"] and MENU[instruction]["ingredients"]['coffee'] < resources["coffee"]:
                instructions = False
            compare()
    print("insert coin")
    quarters = int(input("quarters quantities"))
    dimes = int(input("dimes quantities"))
    nickles = int(input("nickles quantities"))
    pennies = int(input("pennies quantities"))
    coin_management(quarters,dimes,nickles,pennies)
    off = input("Turn off the Coffee Machine by entering “off”").lower()
    if off == "off":
        machine_strat = False
        print('machine off')