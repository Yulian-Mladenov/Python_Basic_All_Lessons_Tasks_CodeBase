required_money_for_the_journey = float(input())
available_cash = float(input())
days_counter = 0
total_of_amount_variable = 0
spending_days_counter = 0

while True:
    action = input()
    amount = float(input())
    total_of_amount_variable = amount
    days_counter += 1
    if action == "spend":
        spending_days_counter += 1
        available_cash -= amount
        if spending_days_counter > 5:
            print("You can't save the money.")
            print(f"{days_counter}")
            break
    if available_cash - amount < 0:
        available_cash = 0
    else:
        available_cash -= amount

    if action == "save":
        spending_days_counter = 0
    if total_of_amount_variable + available_cash == required_money_for_the_journey:
        print(f"You saved the money for {days_counter} days.")
        break
