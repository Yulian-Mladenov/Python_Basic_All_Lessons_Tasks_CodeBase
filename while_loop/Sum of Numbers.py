initial_number = int(input())

total_sum = 0

while True:
    number = int(input())
    total_sum += number
    if total_sum >= initial_number:
        print(total_sum)
        break

