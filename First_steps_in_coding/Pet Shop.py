quantity_dog_food = int(input())
quantity_cat_food = int(input())

price_per_package_cat_food = 4
price_per_package_dog_food = 2.50

total_amount = (quantity_dog_food * price_per_package_dog_food) + (quantity_cat_food * price_per_package_cat_food)
print(f"{total_amount} lv.")
