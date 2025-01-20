# My first approach. Cover betwenn 50-60 % of the task according Chat GPT opinion.
# while True:
#     number = input()
#     if number == "stop":
#         break
#     elif int(number) < 0:
#         print("Number is negative.")
#Here is missung the operator "continue" which is neccesery to skip all the code if the number is negative.
#This skip is necessary to not loose time to execute all the code down below. It simply return to the begging of the loop and waiting for new number.

#     natural_number = 0
#     not_natural_number = 0
#     parsing_data = int(number)
#     if parsing_data > 1:
#         if parsing_data % 1 == 0 and parsing_data % parsing_data == 0:
#             natural_number += parsing_data
#
#     elif parsing_data % 1 != 0 and parsing_data % parsing_data != 0:
#         not_natural_number += parsing_data
#
#
# print(f'"Sum of all prime numbers is: {natural_number}"')
# print(f"Sum of all non prime numbers is: {not_natural_number}")

sum_prime_numbers = 0
sum_non_prime_numbers = 0

while True:
    non_prime_number = False
    new_input = input()
    if new_input == "stop":
        break

    new_number = int(new_input)

    if new_number < 0:
        print("Number is negative.")
        continue

    if new_number <= 1:
        sum_non_prime_numbers += new_number
        non_prime_number = True

    else:
        for number in range(2, int(new_number ** 0.5) + 1):
            if new_number % number == 0:
                sum_non_prime_numbers += new_number
                non_prime_number = True
                break

    if not non_prime_number:
        sum_prime_numbers += new_number

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")
