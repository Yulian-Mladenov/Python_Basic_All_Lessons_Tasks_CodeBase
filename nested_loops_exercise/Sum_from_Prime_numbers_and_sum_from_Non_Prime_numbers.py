
# The prototype of my first approach.
# My first approach. Cover betwenn 50-60 % of the task according Chat GPT opinion.

# natural_number = 0
# not_natural_number = 0
#
# while True:
#     number = input()
#     if number == "stop":
#         break
#     elif int(number) < 0:
#         print("Number is negative.")

#

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




# the teacher approach

prime_number_sum = 0
non_prime_number_sum = 0

while True:
    non_prime_number = False
    old_input = input()
    if old_input == "stop":
        break

    new_input = int(old_input)

    if new_input < 0:
        print("Number is negative.")

    if new_input <= 1:
        non_prime_number_sum += new_input # here need another new variable because maybe will return error. Because is not clear the value of which variable to use.
# the variable on line 45 is a str type or the variable of line 49 which is a int type!
        non_prime_number = True





