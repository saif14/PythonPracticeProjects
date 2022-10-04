import menu as mn

machine_inputs = {
    "water": 600,
    "milk": 500,
    "coffee": 760,
    "money": 0.0
}

coin_insert = {
    "quarter": 0,
    "dime": 0,
    "nickle": 0,
    "pennies": 0
}


def process_coin(required_money):
    calculate_money = 0.25 * coin_insert["quarter"] + 0.1 * coin_insert["dime"] + 0.05 * coin_insert["nickle"] + 0.01 * \
                  coin_insert["pennies"]
    return calculate_money


def insert_money():
    coin_insert["quarter"] = int(input("Number of Quarter: "))
    coin_insert["dime"] = int(input("Number of Dime: "))
    coin_insert["nickle"] = int(input("Number of Nickle: "))
    coin_insert["pennies"] = int(input("Number of Pennies: "))


def check_resources(option):
    status = True
    water = mn.MENU[option]["ingredients"]["water"]
    milk = mn.MENU[option]["ingredients"].get("milk", 0)
    coffee = mn.MENU[option]["ingredients"]["coffee"]
    money = mn.MENU[option]["cost"]

    if machine_inputs["water"] < water or machine_inputs["milk"] < milk or machine_inputs["coffee"] < coffee:
        output = "Sorry there is not enough"
        if machine_inputs["water"] < water:
            output += " water"
        if machine_inputs["milk"] < milk:
            output += " milk"
        if machine_inputs["coffee"] < coffee:
            output += " coffee"
        print(output)
    else:
        machine_inputs["water"] -= water
        machine_inputs["milk"] -= milk
        machine_inputs["coffee"] -= coffee
        insert_money()
        calculated_money = process_coin(money)
        if calculated_money >= money:
            if calculated_money-money > 0:
                print(f"Here is ${calculated_money-money:.2f} in change")
                machine_inputs["money"] += calculated_money
        else:
            print("Sorry that's not enough money. Money refunded")


def make_coffee(option):
    if option == "espresso" or option == "latte" or option == "cappuccino":
        check_resources(option)
    else:
        print("You have given worng input")


def start_machine():

    is_machine_on = True

    while is_machine_on:
        option = input("What would  you like? (espresso/latte/cappuccino):\n")

        if option == "report":
            print(f"Water: {machine_inputs['water']}")
            print(f"Milk: {machine_inputs['milk']}")
            print(f"Coffee: {machine_inputs['coffee']}")
            print(f"Money: {machine_inputs['money']}")
            es = mn.MENU["espresso"]["ingredients"]["water"]
            print(f"Es: {es}")
        elif option == "off":
            is_machine_on = False
            print("Machine is turning off")
        else:
            make_coffee(option)
