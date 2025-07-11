flower_type = input()
Number_of_flowers = float(input())
Budget = float(input())

flower_price = 0

if flower_type == "Roses":
    flower_price = 5
elif flower_type == "Dahlias":
    flower_price = 3.80
elif flower_type == "Tulips":
    flower_price = 2.80
elif flower_type == "Narcissus":
    flower_price = 3
elif flower_type == "Gladiolus":
    flower_price = 2.50

price_before_discount = Number_of_flowers * flower_price
price_after_discount = 0

if flower_type == "Roses":
    if Number_of_flowers > 80:
        price_after_discount = price_before_discount - (price_before_discount * 0.10)

elif flower_type == "Dahlias":
    if Number_of_flowers > 90:
        price_after_discount = price_before_discount - (price_before_discount * 0.15)

elif flower_type == "Tulips":
    if Number_of_flowers > 80:
        price_after_discount = price_before_discount - (price_before_discount * 0.15)

elif flower_type == "Narcissus":
    if Number_of_flowers < 120:
        price_after_discount = price_before_discount + (price_before_discount * 0.15)

elif flower_type == "Gladiolus":
    if Number_of_flowers < 80:
        price_after_discount = price_before_discount + (price_before_discount * 0.20)

else:
    price_before_discount = Number_of_flowers * flower_price


if Budget >= price_after_discount:
    difference = Budget - price_after_discount
    print(f"Hey, you have a great garden with {Number_of_flowers} {flower_type} and {difference:.2f} leva left.")
else:
    difference = price_after_discount - Budget
    print(f"Not enough money, you need {difference:.2f} leva more.")

