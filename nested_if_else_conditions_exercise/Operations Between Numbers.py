number_1 = int(input())
number_2 = int(input())
mathematical_operator = input()

if number_1 == 0:
    print(f"Cannot divide {number_1} by zero")
    exit(0)
elif number_2 == 0:
    print(f"Cannot divide {number_1} by zero")
    exit(0)


result = 0
odd_or_even = ''

if mathematical_operator == '+':
    result = number_1 + number_2
    if result % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'

elif mathematical_operator == '-':
    result = number_1 - number_2
    if result % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'

elif mathematical_operator == '*':
    result = number_1 * number_2
    if result % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'

elif mathematical_operator == '/':
    result = number_1 / number_2

elif mathematical_operator == '%':
    result = abs(number_1 % number_2)

# with this code print one - at the end. Why?
# if mathematical_operator == '+' or '-' or '*':
#     print(f"{number_1} {mathematical_operator} {number_2} = {result} - {odd_or_even}")
# else:
#     print(f"{number_1} {mathematical_operator} {number_2} = {result}")

# with this code all is ok, why?
if mathematical_operator != '+' or '-' or '*':
    print(f"{number_1} {mathematical_operator} {number_2} = {result}")
else:
    print(f"{number_1} {mathematical_operator} {number_2} = {result} - {odd_or_even}")
