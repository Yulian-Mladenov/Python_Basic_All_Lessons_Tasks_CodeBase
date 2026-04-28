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

        # ако spending_days_counter == 5 → печатай и break

    if action == "save":
        spending_days_counter = 0
        # добавя към available_cash

    # ако available_cash >= required_money → печатай и break
