# type_flower = input()
# flowers_quantity = int(input())
# budget = int(input())
#
# rose = 5
# dalia = 3.80
# lale = 2.80
# narcis = 3
# gladiola = 2.50
#
# total_price = 0
#
# if type_flower == "rose" and flowers_quantity > 80:
#     total_price = (rose * flowers_quantity) - total_price * 0.10
# elif type_flower == "rose" and flowers_quantity <= 80:
#     total_price = rose * flowers_quantity
#
# difference = abs(budget - total_price)
#
# if budget < total_price:
#     print(f"Not enough money, you need {difference:.2f} leva more.")
# else:
#     print(f"Hey, you have a great garden with {flowers_quantity} {type_flower} and {difference:.2f} leva left.")
#
#


type_flower = input()
flowers_quantity = int(input())
budget = int(input())

Roses = 5
Dahlias = 3.80
Tulips = 2.80
Narcissus = 3
Gladiolus = 2.50

Roses_price = flowers_quantity * Roses
Dahlias_price = flowers_quantity * Dahlias
Tulips_price = flowers_quantity * Tulips
Narcissus_price = flowers_quantity * Narcissus
Gladiolus_price = flowers_quantity * Gladiolus

Roses_discount = Roses_price - (Roses_price * 0.10)
Dahlias_discount = Dahlias_price - (Dahlias_price * 0.15)
Tulips_discount = Tulips_price - (Tulips_price * 0.15)
Narcissus_discount = Narcissus_price + (Narcissus_price * 0.15)
Gladiolus_discount = Gladiolus_price + (Gladiolus_price * 0.20)

total_price = 0

if type_flower == "Roses":
    if flowers_quantity > 80:
        total_price = Roses_discount
    else:
        total_price = Roses_price

elif type_flower == "Dahlias":
    if flowers_quantity > 90:
        total_price = Dahlias_discount
    else:
        total_price = Dahlias_price

elif type_flower == "Tulips":
    if flowers_quantity > 80:
        total_price = Tulips_discount
    else:
        total_price = Tulips_price

elif type_flower == "Narcissus":
    if flowers_quantity < 120:
        total_price = Narcissus_discount
    else:
        total_price = Narcissus_price

elif type_flower == "Gladiolus":
    if flowers_quantity < 80:
        total_price = Gladiolus_discount
    else:
        total_price = Gladiolus_price

difference = abs(budget - total_price)

if budget < total_price:
    print(f"Not enough money, you need {difference:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {flowers_quantity} {type_flower} and {difference:.2f} leva left.")


