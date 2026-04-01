text = input()

total_sum = 0

for iteration in text:
    if iteration == 'a':
        total_sum += 1
    elif iteration == 'e':
        total_sum += 2
    elif iteration == 'i':
        total_sum += 3
    elif iteration == 'o':
        total_sum += 4
    elif iteration == 'u':
        total_sum += 5

print(total_sum)


