range_number = int(input())

till_200 = 0
from_200_to_399 = 0
from_400_to_599 = 0
from_600_to_799 = 0
above_800 = 0
HUNDRED = 100

for iterator in range(range_number):
    number = int(input())
    if number < 200:
        till_200 += 1
    elif 200 <= number < 400:
        from_200_to_399 += 1
    elif 400 <= number < 600:
        from_400_to_599 += 1
    elif 600 <= number < 800:
        from_600_to_799 += 1
    elif number >= 800:
        above_800 += 1

percentage_till_200 = (till_200 / range_number) * HUNDRED
percentage_from_200_to_399 = (from_200_to_399 / range_number) * HUNDRED
percentage_from_400_to_599 = (from_400_to_599 / range_number) * HUNDRED
percentage_from_600_to_799 = (from_600_to_799 / range_number) * HUNDRED
percentage_above_800 = (above_800 / range_number) * HUNDRED

print(f"{percentage_till_200:.2f}%")
print(f"{percentage_from_200_to_399:.2f}%")
print(f"{percentage_from_400_to_599:.2f}%")
print(f"{percentage_from_600_to_799:.2f}%")
print(f"{percentage_above_800:.2f}%")

