number = int(input())
combination_counter = 0

for x1 in range(number + 1):
    for x2 in range(number + 1):
        for x3 in range(number + 1):
            total_sum = x1 + x2 + x3
            if total_sum == number:
                combination_counter += 1

print(combination_counter)
