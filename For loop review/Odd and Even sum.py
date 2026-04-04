input_number = int(input())

odd_numbers_sum = 0
even_numbers_sum = 0

for index in range(1, input_number + 1):
    numbers = int(input())
    if index % 2 == 0:
        even_numbers_sum += numbers
    else:
        odd_numbers_sum += numbers

if odd_numbers_sum == even_numbers_sum:
    print('Yes')
    print(f'Sum = {odd_numbers_sum}')
else:
    print('No')
    print(f'Diff = {abs(odd_numbers_sum - even_numbers_sum)}')
