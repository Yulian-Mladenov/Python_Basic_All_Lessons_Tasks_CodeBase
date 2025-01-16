number = int(input())

for row in range(1, number + 1):
    for numbers in range(1, row + 1):
        print(f'{numbers}', end='')
    print()