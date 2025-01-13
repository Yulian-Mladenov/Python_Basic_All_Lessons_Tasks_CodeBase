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

total_price = (number_of_trucks * truck) + (number_of_minions * minion) + \
              (number_of_bears * bear) + (number_of_dolls * doll) + (number_of_puzzles * puzzle)

total_quantity = number_of_trucks + number_of_minions + number_of_puzzles +\
                 + number_of_dolls + number_of_bears

discount = total_price * 0.25

if total_quantity >= 50:
    total_price = total_price - discount
else:
    total_price = total_price

#с две променливи за намиране на нетния приход дава 100 точки в Джъдж.
#total_profit_after_rent = total_price - (total_price * 0.10)
#total_net_profit = abs(total_profit_after_rent - price_of_excursion)

#с една променлива за намиране на нетния приход дава 60 точки в Джъдж.
total_net_profit = abs((total_price - (total_price * 0.10)) - price_of_excursion)

if total_net_profit >= price_of_excursion:
    print(f"Yes! {total_net_profit:.2f} lv left.")
else:
    print(f"Not enough money! {total_net_profit:.2f} lv needed.")


