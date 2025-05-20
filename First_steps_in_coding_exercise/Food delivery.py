chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery_price = 2.50
desert_price_in_percentage = 0.20

number_chicken_meals = int(input())
number_fish_meals = int(input())
number_vegetarian_meals = int(input())

total_food_price = (number_vegetarian_meals * vegetarian_menu) + (number_fish_meals * fish_menu) + (number_chicken_meals * chicken_menu)
total_food_price_with_desert = (total_food_price * desert_price_in_percentage) + total_food_price
total_food_price_with_delivery_price = total_food_price_with_desert + delivery_price

print(f'{total_food_price_with_delivery_price:.2f}')

