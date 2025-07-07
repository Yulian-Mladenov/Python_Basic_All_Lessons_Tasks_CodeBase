# this is my first try after monts without to coding.
# destination = input()
# minimal_budget = float(input())
#
# while False:
#     add_money = float(input())
#     final_amount += add_money
#     if final_amount >= necesery_budget:
#         print('go to travel')
#         break


# this is fully working code
while True:
    destination = input("Enter destination (or 'End' to stop): ")
    if destination == "End":
        break  # Exit the loop if input is 'End'

    minimal_budget = float(input(f"Enter the budget needed for {destination}: "))
    final_amount = 0.0  # Initialize the savings for the current destination

    while final_amount < minimal_budget:
        add_money = float(input("Enter saved amount: "))
        final_amount += add_money

        if final_amount >= minimal_budget:
            print(f"Going to {destination}!")
            break





