# The prototype of my first approach.
# My first approach. Cover between 50-60 % of the task according Chat GPT opinion.

# natural_number = 0
# not_natural_number = 0
#
# while True:
#     number = input()
#     if number == "stop":
#         break
#     elif int(number) < 0:
#         print("Number is negative.")

#Here is missung the operator "continue" which is neccesery to skip all the code if the number is negative.
#This skip is necessary to not loose time to execute all the code down below. It simply return to the begging of the loop and waiting for new number.

#     parsing_data = int(number)
#     if parsing_data > 1:
#         if parsing_data % 1 == 0 and parsing_data % parsing_data == 0: # here is error in the logic to find prime and non prime numbers
#             natural_number += parsing_data
#
#     elif parsing_data % 1 != 0 and parsing_data % parsing_data != 0:
#         not_natural_number += parsing_data
#
#
# print(f'"Sum of all prime numbers is: {natural_number}"')
# print(f"Sum of all non prime numbers is: {not_natural_number}")




# the teacher approach

# sum_prime_numbers = 0
# sum_non_prime_numbers = 0
#
# while True:
#     non_prime_number = False
#     new_input = input()
#     if new_input == "stop":
#         break
#
#     new_number = int(new_input)
#
#     if new_number < 0:
#         print("Number is negative.")
#         continue
#
#     if new_number <= 1:
#         sum_non_prime_numbers += new_number
#         non_prime_number = True
#
#     else:
#         for number in range(2, int(new_number ** 0.5) + 1):
#             if new_number % number == 0:
#                 sum_non_prime_numbers += new_number
#                 non_prime_number = True
#                 break
#
#     if not non_prime_number:
#         sum_prime_numbers += new_number
#
# print(f"Sum of all prime numbers is: {sum_prime_numbers}")
# print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")


# This is ChatGPT approach, without to sum the numbers, just showing after each loop the number is prime or not.
# import math
#
# number = int(input("Enter a number: "))
# is_prime = True
#
# if number < 2:
#     is_prime = False
# else:
#     for i in range(2, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             is_prime = False
#             break
#
# if is_prime:
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")


# Правилото е, просто число е число по-голямо от 1 и се дели без остатък само на 1 и на себе си.
# Така че, всички цифри и числа които се делят без остатък и на други цифри и числи освен 1 и самото число не са прости.
# Така че, ако един делител се дели на квадратния корен на числото което се чудим дали е просто или не без остатък,
# то тогава това число не е просто, защото сме намерили трети делител който се дели без осататък, освен 1 и него самото.


n = 10
total = sum(range(1, n + 1))
print(f"The sum of the first {n} numbers is {total}.")
