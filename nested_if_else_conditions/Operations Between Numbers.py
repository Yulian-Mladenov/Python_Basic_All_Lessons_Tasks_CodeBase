import time
start = time.time()
# this code return 90 from 100 points
# data reading
number_1 = int(input())
number_2 = int(input())
operator = input()

# variables for calculations
Sum = 0
Type = ""

# if statements and result printing
if operator == "+":
    Sum = number_1 + number_2
    if Sum % 2 == 0:
        Type = "even"
    else:
        Type = "odd"
    print(f"{number_1} {operator} {number_2} = {Sum} - {Type}")

elif operator == "-":
    Sum = abs(number_1 - number_2)
    if Sum % 2 == 0:
        Type = "even"
    else:
        Type = "odd"
    print(f"{number_1} {operator} {number_2} = {Sum} - {Type}")

elif operator == "*":
    Sum = number_1 * number_2
    if Sum % 2 == 0:
        Type = "even"
    else:
        Type = "odd"
    print(f"{number_1} {operator} {number_2} = {Sum} - {Type}")

elif operator == "/" and number_1 and number_2 != 0:
    Sum = abs(number_1 / number_2)
    print(f"{number_1} / {number_2} = {Sum:.2f}")

elif operator == "%" and number_1 and number_2 != 0:
    Sum = abs(number_1 % number_2)
    print(f"{number_1} % {number_2} = {Sum}")

else:
    print(f"Cannot divide {number_1} by zero")

print(f'Time: {time.time() - start:.4f}')


# import time
# start = time.time()
# # entrance data reading
# first_number = int(input())
# second_number = int(input())
# operator = input().strip()
#
# # this statement cover the condition when the number cannot be divide by 0= is written at the top of the code,
# # because to be faster.If this case appear first,so the program will return that is not possible to divide on 0 and
# # will terminate will the special answer. in my code upper,this code-block is on the end of the code.So in this case
# # every time the IDE must pass through all the code to print that on 0 cannot divide,which is execute time longer
# # consumption.
# if second_number == 0 and (operator == "/" or operator == "%"):
#     print(f"Cannot divide {first_number} by zero")
#     exit()
#
# # here is the main if-else check moment,to filtrate the math according the sign.
# result = 0
# if operator == "+":
#     result = first_number + second_number
# elif operator == "-":
#     result = first_number - second_number
# elif operator == "*":
#     result = first_number * second_number
# elif operator == "/":
#     result = first_number / second_number
# elif operator == "%":
#     result = first_number % second_number
#
# # here is the final filtration to find even or odd and print the final result
# if operator == "+" or operator == "-" or operator == "*":
#     even_or_odd = "odd"
#     if result % 2 == 0:
#         even_or_odd = "even"
#     print(f"{first_number} {operator} {second_number} = {result} - {even_or_odd}")
# elif operator == "/":
#     print(f"{first_number} / {second_number} = {result:.2f}")
# elif operator == "%":
#     print(f"{first_number} % {second_number} = {result}")

# print(f'Time: {time.time() - start:.4f}')




