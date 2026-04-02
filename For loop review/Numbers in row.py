numbers = int(input())

max_number = 0
min_number = 0

for index in range(numbers):
    number = int(input())
    if number > min_number:
        max_number += number
    elif number > max_number:
        min_number += number

print(int(max_number))
print(int(min_number))
