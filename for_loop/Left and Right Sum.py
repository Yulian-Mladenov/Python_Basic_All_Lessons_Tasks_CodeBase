# number = int(input())
#
# total = 0
#
# for index in range(number):
#     new_number = int(input())
#     total += new_number

n = int(input())

total_left_sum = 0
total_right_sum = 0

for index in range(0, n):
    left_sum = int(input())
    total_left_sum += left_sum
# print(total_left_sum)

for index in range(0, n):
    right_sum = int(input())
    total_right_sum += right_sum

difference = abs(total_left_sum - total_right_sum)

if total_right_sum == total_left_sum:
    print(f"Yes, sum = {total_left_sum}")
else:
    print(f"No, diff = {difference}")

