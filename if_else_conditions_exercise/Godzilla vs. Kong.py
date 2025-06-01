movie_budget = float(input())
number_statist = int(input())
price_to_wearing_one_statist = float(input())

decoration_price = movie_budget * 0.10

price_to_wear_all_statist = number_statist * price_to_wearing_one_statist

if number_statist > 150:
    price_to_wear_all_statist = price_to_wear_all_statist - (price_to_wear_all_statist * 0.10)

total_costs = price_to_wear_all_statist + decoration_price

difference = abs(total_costs - movie_budget)

if total_costs > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")


# budget = float(input())
# number_of_people = int(input())
# price_for_one_person = float(input())
#
# decoration = (budget * 0.10)
#
# first_price_for_statists = price_for_one_person * number_of_people
#
# if number_of_people > 150:
#     first_price_for_statists = first_price_for_statists - (first_price_for_statists * 0.10)
# else:
#     first_price_for_statists = first_price_for_statists
#
# not_enough_money = abs((first_price_for_statists + decoration) - budget)
#
# if decoration + first_price_for_statists > budget:
#     print('Not enough money!')
#     print(f"Wingard needs {not_enough_money:.2f} leva more.")
# elif decoration + first_price_for_statists <= budget:
#     print("Action!")
#     print(f"Wingard starts filming with {not_enough_money:.2f} leva left.")

