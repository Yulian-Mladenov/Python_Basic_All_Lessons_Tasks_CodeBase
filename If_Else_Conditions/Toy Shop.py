price_of_excursion = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

puzzle = 2.60
doll = 3
bear = 4.10
minion = 8.20
truck = 2

#общо количество
total_quantity = number_of_trucks + number_of_minions + number_of_puzzles +\
                 + number_of_dolls + number_of_bears

#обща печалба
bruto_profit = (number_of_trucks * truck) + (number_of_minions * minion) + \
              (number_of_bears * bear) + (number_of_dolls * doll) + (number_of_puzzles * puzzle)

#изчисление на отстъпка
discount = bruto_profit * 0.25

#проверка в коя печалба влиза
if total_quantity >= 50:
    bruto_profit = bruto_profit - discount
else:
    bruto_profit = bruto_profit

#нетна печалба след всички разходи
net_profit = abs((bruto_profit - (bruto_profit * 0.10)) - price_of_excursion)

#крайна проверка преди печатане на резултат
if net_profit >= price_of_excursion:
    print(f'Yes! {net_profit:.2f} lv left.')
else:
    print(f"Not enough money! {net_profit:.2f} lv needed.")


