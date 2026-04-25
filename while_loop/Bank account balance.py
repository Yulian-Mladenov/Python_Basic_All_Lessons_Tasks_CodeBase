total_amount = 0

while True:
    initial_amount = input()
    if initial_amount == "NoMoreMoney":
        print(f"Total: {total_amount:.2f}")
        break

    if float(initial_amount) < 0:
        print("Invalid operation!")
        print(f"Total: {total_amount:.2f}")
        break
    else:
        initial_amount = float(initial_amount)
        total_amount += initial_amount
        print(f"Increase: {initial_amount:.2f}")


