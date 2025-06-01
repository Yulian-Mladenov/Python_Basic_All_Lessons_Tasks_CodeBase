price_of_vacation = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

puzzle_price = 2.60
speaking_doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2

total_price = (number_of_puzzles * puzzle_price) + (number_of_dolls * speaking_doll) + \
              (number_of_teddy_bears * teddy_bear) + (number_of_minions * minion) + (number_of_trucks * truck)

total_number_of_toys = number_of_trucks + number_of_puzzles + \
                       number_of_minions + number_of_dolls + number_of_teddy_bears

if total_number_of_toys >= 50:
    total_price -= (total_price * 0.25)

total_price_without_rent = total_price - (total_price * 0.10)

difference = abs(total_price_without_rent - price_of_vacation)

if total_price_without_rent >= price_of_vacation:
    print(f"Yes! {difference:.2f} lv left.")
elif total_price_without_rent < price_of_vacation:
    print(f"Not enough money! {difference:.2f} lv needed.")




# Toy prices (BGN)
# puzzle = 2.60
# talking_doll = 3
# teddy_bear = 4.10
# minion = 8.20
# truck = 2
#
# vacation_price = float(input())
# puzzle_quantity = int(input())
# talking_doll_quantity = int(input())
# teddy_bear_quantity = int(input())
# minion_quantity = int(input())
# truck_quantity = int(input())
#
# puzzles_price = puzzle*puzzle_quantity
# talking_dolls_price = talking_doll * talking_doll_quantity
# teddy_bears_price = teddy_bear * teddy_bear_quantity
# minions_price = minion * minion_quantity
# trucks_price = truck * truck_quantity
#
# total_price = puzzles_price + talking_dolls_price + teddy_bears_price + minions_price + trucks_price
#
# toys_quantity = puzzle_quantity + talking_doll_quantity + teddy_bear_quantity + minion_quantity + truck_quantity
# final_price = total_price
# if toys_quantity >= 50:
#     final_price = total_price - (total_price*0.25)
#
# money_earned = final_price - (final_price * 0.10)
#
# if money_earned >= vacation_price:
#     print(f"Yes! {money_earned-vacation_price:0.2f} lv left.")
# elif money_earned < vacation_price:
#     print(f"Not enough money! {vacation_price - money_earned:0.2f} lv needed.")