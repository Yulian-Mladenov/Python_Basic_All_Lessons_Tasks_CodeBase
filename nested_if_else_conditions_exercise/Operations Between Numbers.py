# this is my first solution. Is not working full correctlly. The problems are in lines 6 till 11 and lines 50 till 53.
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
if mathematical_operator == '+' or '-' or '*':
    print(f"{number_1} {mathematical_operator} {number_2} = {result} - {odd_or_even}")
else:
    print(f"{number_1} {mathematical_operator} {number_2} = {result}")




# This is Claude AI solution completely working - return 100 points.

number_1 = int(input())
number_2 = int(input())
mathematical_operator = input()

if number_2 == 0 and (mathematical_operator == '/' or mathematical_operator == '%'):
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
    result = number_1 % number_2

# Fixed condition - now correctly checks for +, -, *
if mathematical_operator in ['+', '-', '*']:
    print(f"{number_1} {mathematical_operator} {number_2} = {result} - {odd_or_even}")
elif mathematical_operator == '/':
    print(f"{number_1} / {number_2} = {result:.2f}")
else:  # modulo operation
    print(f"{number_1} % {number_2} = {result}")


# third attempt return 100 points:
number_1 = int(input())
number_2 = int(input())
mathematical_operator = input()

if number_2 == 0 and (mathematical_operator == '/' or mathematical_operator == '%'):
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
    result = number_1 % number_2

# Fixed condition - now correctly checks for +, -, *
if mathematical_operator == '+' or mathematical_operator == '-' or mathematical_operator == '*':
    print(f"{number_1} {mathematical_operator} {number_2} = {result} - {odd_or_even}")
elif mathematical_operator == '/':
    print(f"{number_1} / {number_2} = {result:.2f}")
else:  # modulo operation
    print(f"{number_1} % {number_2} = {result}")
