# this code have a problem with the first test case and very probablly with cases that no exists in the task but only in Judge.
# The problem began on line 47 where the price is all time after discount. And when need price before discount there is no data.
# flower_type = input()
# Number_of_flowers = float(input())
# Budget = float(input())
#
# flower_price = 0
#
# if flower_type == "Roses":
#     flower_price = 5
# elif flower_type == "Dahlias":
#     flower_price = 3.80
# elif flower_type == "Tulips":
#     flower_price = 2.80
# elif flower_type == "Narcissus":
#     flower_price = 3
# elif flower_type == "Gladiolus":
#     flower_price = 2.50
#
# price_before_discount = Number_of_flowers * flower_price
# price_after_discount = 0
#
# if flower_type == "Roses":
#     if Number_of_flowers > 80:
#         price_after_discount = price_before_discount - (price_before_discount * 0.10)
#
# elif flower_type == "Dahlias":
#     if Number_of_flowers > 90:
#         price_after_discount = price_before_discount - (price_before_discount * 0.15)
#
# elif flower_type == "Tulips":
#     if Number_of_flowers > 80:
#         price_after_discount = price_before_discount - (price_before_discount * 0.15)
#
# elif flower_type == "Narcissus":
#     if Number_of_flowers < 120:
#         price_after_discount = price_before_discount + (price_before_discount * 0.15)
#
# elif flower_type == "Gladiolus":
#     if Number_of_flowers < 80:
#         price_after_discount = price_before_discount + (price_before_discount * 0.20)
#
# else:
#     price_before_discount = Number_of_flowers * flower_price
#
#
# if Budget >= price_after_discount:
#     difference = Budget - price_after_discount
#     print(f"Hey, you have a great garden with {Number_of_flowers} {flower_type} and {difference:.2f} leva left.")
# else:
#     difference = price_after_discount - Budget
#     print(f"Not enough money, you need {difference:.2f} leva more.")
#


flower_type = input()
Number_of_flowers = int(input())
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

price = Number_of_flowers * flower_price

if flower_type == "Roses":
    flower_price = 5
    if Number_of_flowers > 80:
        price -= (price * 0.10)
    else:
        price = Number_of_flowers * flower_price

elif flower_type == "Dahlias":
    if Number_of_flowers > 90:
        price -= (price * 0.15)
    else:
        price = Number_of_flowers * flower_price

elif flower_type == "Tulips":
    if Number_of_flowers > 80:
        price -= (price * 0.15)
    else:
        price = Number_of_flowers * flower_price

elif flower_type == "Narcissus":
    if Number_of_flowers < 120:
        price += (price * 0.15)
    else:
        price = Number_of_flowers * flower_price

elif flower_type == "Gladiolus":
    if Number_of_flowers < 80:
        price += (price * 0.20)
    else:
        price = Number_of_flowers * flower_price


if Budget >= price:
    difference = Budget - price
    print(f"Hey, you have a great garden with {Number_of_flowers} {flower_type} and {difference:.2f} leva left.")
else:
    difference = price - Budget
    print(f"Not enough money, you need {difference:.2f} leva more.")

