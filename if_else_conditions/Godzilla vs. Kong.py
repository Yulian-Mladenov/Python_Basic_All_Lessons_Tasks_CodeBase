budget = float(input())
number_of_people = int(input())
price_for_one_person = float(input())

decoration = (budget * 0.10)

first_price_for_statists = price_for_one_person * number_of_people

if number_of_people > 150:
    first_price_for_statists = first_price_for_statists - (first_price_for_statists * 0.10)
else:
    first_price_for_statists = first_price_for_statists

not_enough_money = abs((first_price_for_statists + decoration) - budget)

if decoration + first_price_for_statists > budget:
    print('Not enough money!')
    print(f"Wingard needs {not_enough_money:.2f} leva more.")

elif decoration + first_price_for_statists <= budget:
    print("Action!")
    print(f"Wingard starts filming with {not_enough_money:.2f} leva left.")



