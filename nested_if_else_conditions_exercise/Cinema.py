premiere_price = 12
normal_price = 7.50
discount_price = 5

type_of_movie = input()
number_of_lines = int(input())
number_of_columns = int(input())

total_number_of_places = number_of_columns * number_of_lines
total_profit = 0

if type_of_movie == 'Premiere':
    total_profit = total_number_of_places * premiere_price
elif type_of_movie == 'Normal':
    total_profit = total_number_of_places * normal_price
elif type_of_movie == 'Discount':
    total_profit = total_number_of_places * discount_price

print(f'{total_profit:.2f} leva')


