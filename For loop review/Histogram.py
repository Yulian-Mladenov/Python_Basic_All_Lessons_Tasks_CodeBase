import time
start = time.time()

number_of_numbers = int(input())

counter_less_than_200 = 0    # first group
counter_between_200_and_399 = 0     # second group
counter_between_400_and_599 = 0     # third group
counter_between_600_and_799 = 0     # fourth group
counter_more_than_800_included = 0      # fifth group

for number in range(number_of_numbers):
    numbers = int(input())
    if numbers < 200:
        counter_less_than_200 += 1
    elif 200 <= numbers <= 399:
        counter_between_200_and_399 += 1
    elif 400 <= numbers <= 599:
        counter_between_400_and_599 += 1
    elif 600 <= numbers <= 799:
        counter_between_600_and_799 += 1
    elif numbers >= 800:
        counter_more_than_800_included += 1

percentage_of_first_group = counter_less_than_200 / number_of_numbers * 100
percentage_of_second_group = counter_between_200_and_399 / number_of_numbers * 100
percentage_of_third_group = counter_between_400_and_599 / number_of_numbers * 100
percentage_of_four_group = counter_between_600_and_799 / number_of_numbers * 100
percentage_of_five_group = counter_more_than_800_included / number_of_numbers * 100

print(f'{percentage_of_first_group:.2f}%')
print(f'{percentage_of_second_group:.2f}%')
print(f'{percentage_of_third_group:.2f}%')
print(f'{percentage_of_four_group:.2f}%')
print(f'{percentage_of_five_group:.2f}%')

end = time.time()
print(f"Време за изпълнение: {end - start} секунди")



