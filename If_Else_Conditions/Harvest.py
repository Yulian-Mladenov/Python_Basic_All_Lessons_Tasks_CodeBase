#read user data
x_meters = int(input())
y_fruits_from_1mq = float(input())
z_necesery_wine = int(input())
workers = int(input())

#math calculations
import math
NECESARY_FRUIT_FOR_LITER = 2.5
total_fruit = x_meters * y_fruits_from_1mq
percentage_for_wine = total_fruit * 0.40
total_wine = percentage_for_wine / NECESARY_FRUIT_FOR_LITER
enough_or_not_wine = math.floor(abs((total_wine - z_necesery_wine)))
wine_per_worker = math.ceil(abs(total_wine - z_necesery_wine) / workers)

#final check what and when to print
if total_wine < z_necesery_wine:
    print(f"It will be a tough winter! More {enough_or_not_wine} liters wine needed.")
elif total_wine >= z_necesery_wine:
    print(f"Good harvest this year! Total wine: {total_wine:.0f} liters.")
    print(f"{enough_or_not_wine} liters left -> {wine_per_worker} liters per person.")

