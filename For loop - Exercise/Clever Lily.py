# Lilly_years = int(input())
# washing_machine_price = float(input())
# price_for_one_toy = float(input())
#
# Lilly_brother_stole_money = 1
# EVEN_BIRTHDAY = 10
# even_birthdays_sum = 0
# toys_quantity = 0
# money_from_toys_selling = 0
# birthdays_counter = 0
#
# for iteration in range(1, Lilly_years +1):
#     if iteration % 2 == 0:
#         birthdays_counter += 1
#         even_birthdays_sum += (birthdays_counter * EVEN_BIRTHDAY) - Lilly_brother_stole_money
#     else:
#         toys_quantity += 1
#         money_from_toys_selling = toys_quantity * price_for_one_toy
#
# total_amount_of_money = money_from_toys_selling + even_birthdays_sum
# difference = abs(washing_machine_price - total_amount_of_money)
#
# if total_amount_of_money >= washing_machine_price:
#     print(f"Yes! {difference:.2f}")
# else:
#     print(f"No! {difference:.2f}")
# Time elapsed (hh:mm:ss.ms) 0:00:04.913523

from datetime import datetime
start_time = datetime.now()

age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
savings = 0.0
coefficient = 1

for years in range(1, age +1):
    if years % 2 !=0:
        savings += toy_price
    elif years % 2 == 0:
        savings += (coefficient * 10)
        savings -= 1
        coefficient += 1

if savings >= washing_machine_price:
    print(f"Yes! {(savings - washing_machine_price):.2f}")
else:
    print(f"No! {(washing_machine_price - savings):.2f}")

time_elapsed = datetime.now() - start_time
print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

# Time elapsed (hh:mm:ss.ms) 0:00:04.278548





