#reading user data
days = int(input())
food = int(input())
food_for_dog_per_day = float(input())
food_for_cat_per_day= float(input())
food_for_turtle_per_day = float(input())

#math calculations
total_dog_food = food_for_dog_per_day * days
total_cat_food = food_for_cat_per_day * days
total_turtle_food = (food_for_turtle_per_day * days) / 1000
total_food_for_all = total_turtle_food + total_cat_food + total_dog_food
import math
difference = math.floor(abs(total_food_for_all - food))
difference_2 = math.ceil(abs(total_food_for_all - food))

#final result by if-else check
if total_food_for_all < food:
    print(f"{difference} kilos of food left.")
else:
    print(f"{difference_2} more kilos of food are needed.")