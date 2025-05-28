import math
price_of_one_rocket = float(input())
number_of_the_rockets = int(input())
number_of_pears_of_sneakers = int(input())

total_price_of_the_rockets = price_of_one_rocket * number_of_the_rockets

price_of_one_pear_sneakers = price_of_one_rocket / 6
total_price_of_all_pears_sneakers = price_of_one_pear_sneakers * number_of_pears_of_sneakers

total_price_of_all_sneakers_and_rockets = total_price_of_all_pears_sneakers + total_price_of_the_rockets
additional_equipment_price = total_price_of_all_sneakers_and_rockets * 0.2

final_total_price_of_all_equipment = additional_equipment_price + total_price_of_all_sneakers_and_rockets

djokovic_have_to_pay = final_total_price_of_all_equipment / 8
sponsors_have_to_pay = final_total_price_of_all_equipment - djokovic_have_to_pay

print(f"Price to be paid by Djokovic {math.floor(djokovic_have_to_pay)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_have_to_pay)}")

