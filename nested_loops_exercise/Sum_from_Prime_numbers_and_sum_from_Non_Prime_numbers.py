
# The prototype of my first approach
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


# Second approach
natural_number = 0
not_natural_number = 0

while True:
    number = input()
    if number == "stop":
        break
    elif int(number) < 0:
        print("Number is negative.")

    parsing_data = int(number)
    if parsing_data % 1 == 0 or parsing_data % parsing_data == 0:
        natural_number += parsing_data

    else:
        not_natural_number += parsing_data

print(f'"Sum of all prime numbers is: {natural_number}"')
print(f"Sum of all non prime numbers is: {not_natural_number}")
