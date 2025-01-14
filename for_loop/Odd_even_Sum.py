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