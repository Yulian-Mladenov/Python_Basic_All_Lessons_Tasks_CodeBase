price_per_kilo_vegetables = float(input())
price_per_kilo_fruits = float(input())
total_qt_of_vegetables_in_kg = float(input())
total_qt_of_fruits_in_kg = float(input())

fixed_euro_value = 1.94

total_profit_in_euro = ((total_qt_of_fruits_in_kg * price_per_kilo_fruits) + (total_qt_of_vegetables_in_kg * price_per_kilo_vegetables)) / fixed_euro_value
print(f'{total_profit_in_euro:.2f}')

