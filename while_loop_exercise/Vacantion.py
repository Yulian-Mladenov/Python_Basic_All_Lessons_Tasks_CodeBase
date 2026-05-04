required_money_for_the_journey = float(input())
available_cash = float(input())
days_counter = 0
total_of_amount_variable = 0
spending_days_counter = 0

while True:
    action = input()
    amount = float(input())
    days_counter += 1

    if action == "spend":
        spending_days_counter += 1
        # вади от available_cash, но не под 0
        available_cash -= amount
        if available_cash <= 0:
            available_cash = 0
        # ако spending_days_counter == 5 → печатай и break
        if spending_days_counter == 5:
            print("You can't save the money.")
            print(f"{days_counter}")
            break

    if action == "save":
        spending_days_counter = 0
        # добавя към available_cash
        available_cash += amount

    # ако available_cash >= required_money → печатай и break
    if available_cash >= required_money_for_the_journey:
        print(f"You saved the money for {days_counter} days.")
        break
