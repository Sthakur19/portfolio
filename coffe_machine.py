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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def is_resourse_sufficent(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    '''Return the total calculated from coine  inserted '''
    print("Please insert coin ")
    total = int(input("how may quarters? :")) * 0.25
    total += int(input("how may dimes? :")) * 0.1
    total += int(input("how may nickles  ? :")) * 0.05
    total += int(input("how may pennies? :")) * 0.01
    return total


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resourse_sufficent(drink["ingredients"]):
            payment = process_coin()



