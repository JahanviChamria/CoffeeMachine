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

def resourcesenough(ing):
    for item in ing:
        if ing[item]>resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

should_continue=True
money=0.0
while should_continue:
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        should_continue=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
    else:
        drink=MENU[choice]
        enough=resourcesenough(drink["ingredients"])
        if enough==True:
            print("Please insert coins: ")
            qt=(int(input("Quarters: ")))*0.25
            di=(int(input("Dimes: ")))*0.1
            ni=(int(input("Nickels: ")))*0.05
            pe=(int(input("Pennies: ")))*0.01
            total=qt+di+ni+pe
            if drink["cost"]<=total:
                change=round(total-drink["cost"], 2)
                if change>0.0:
                    print(f"Change= ${change}")
                money=money+drink["cost"]
                for n in drink["ingredients"]:
                    resources[n]=resources[n]-drink["ingredients"][n]
                print(f"Here is your {choice}, enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
