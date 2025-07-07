# number = int(input())
#
# summary = 0
# biggest_number = 0
# difference = abs(biggest_number - summary)
#
# for iterator in range(number):
#     numbers = int(input())
#     summary += numbers
#
# if iterator > summary:
#     biggest_number = iterator
#     print(f"Yes\n Sum = {biggest_number}")
# else:
#     print(f"no\n Diff= {difference}")

# this is the part he reads the initial number and then each his index(iteration)
import sys
number = int(input())

max_number = -sys.maxsize
summary = 0

for iterator in range(number):
    biggest_number = int(input())
    if biggest_number > max_number:
        max_number = biggest_number
    summary += biggest_number

if max_number == (summary - max_number):
    print(f"Yes\n Sum = {max_number}")
else:
    difference = abs(max_number - (summary - max_number))
    print(f"No\n Diff = {difference}")


