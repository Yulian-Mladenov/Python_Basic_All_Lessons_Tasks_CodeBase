target_number = int(input())

left_sum = 0
right_sum = 0

for left_index in range(target_number):
    left_numbers = int(input())
    left_sum += left_numbers

for right_index in range(target_number):
    right_numbers = int(input())
    right_sum += right_numbers

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
elif left_sum != right_sum:
    print(f'No, diff = {abs(left_sum - right_sum)}')


