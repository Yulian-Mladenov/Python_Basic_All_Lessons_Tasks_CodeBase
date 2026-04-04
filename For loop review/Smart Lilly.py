import time
start = time.time()

Lilly_age = int(input())
price_of_wash_machine = float(input())
price_for_one_toy = int(input())

money_from_birthdays = 0
number_of_toys_from_birthdays = 0
number_of_even_birthdays = 0
total_money = 0

for index in range(1, Lilly_age + 1):
    if index % 2 == 0:
        number_of_even_birthdays += 1
        money_from_birthdays = (number_of_even_birthdays * 10) - 1
        total_money += money_from_birthdays
    else:
        number_of_toys_from_birthdays += 1

total_Lilly_money = (number_of_toys_from_birthdays * price_for_one_toy) + total_money

if price_of_wash_machine <= total_Lilly_money:
    print(f"Yes! {total_Lilly_money - price_of_wash_machine:.2f}")
else:
    print(f"No! {price_of_wash_machine - total_Lilly_money:.2f}")

end = time.time()
print(f"Време за изпълнение: {end - start} секунди")



# more optimized approach
# Четем входните данни
age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_money = 0
toys_count = 0
even_birthday_count = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        # Четен рожден ден - получава пари, братът взима 1 лев
        even_birthday_count += 1
        total_money += (even_birthday_count * 10) - 1
    else:
        # Нечетен рожден ден - получава играчка
        toys_count += 1

# Добавяме парите от продадените играчки
total_money += toys_count * toy_price

# Проверяваме дали стигат парите
difference = total_money - washing_machine_price
if difference >= 0:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {abs(difference):.2f}")