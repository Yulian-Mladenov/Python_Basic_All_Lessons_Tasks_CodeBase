# number = int(input())
#
# total_even_sum = 0
# total_odd_sum = 0
#
# for index in range(0, number, +1):
#     even_sum = int(input())
#     even_sum += total_even_sum
#
# for index in range(1, number, +1):
#     odd_sum = int(input())
#     odd_sum += total_odd_sum
#
# difference = abs(total_even_sum - total_odd_sum)
#
# if total_odd_sum == total_even_sum:
#     print(f"Yes\nSum = {total_even_sum}")
# else:
#     print(f"No\nDiff = {difference}")

number = int(input())

odd_sum = 0
even_sum = 0

for index in range(number):
    current_number = int(input())

    if index %2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if odd_sum == even_sum:
    print(f"Yes\nSum = {even_sum}")
else:
    difference = abs(even_sum - odd_sum)
    print(f"No\nDiff = {difference}")
