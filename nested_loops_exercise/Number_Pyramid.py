number = int(input())

counter = 1
is_current_number_bigger_than_number = False

for row in range(1,number + 1):
    for colons in range(1, row + 1):
        if counter > number:
            is_current_number_bigger_than_number = True
            break
        print(str(counter) + ' ', end='')
        counter += 1
    if is_current_number_bigger_than_number is True:
        break
    print()