number_1 = int(input())
number_2 = int(input())

even_elements = 0
odd_elements = 0

for number in range(number_1, number_2 + 1):
    for indexes in range(number):
        if indexes % 2 == 0:
            even_elements += indexes
        else:
            odd_elements += indexes

    if even_elements == odd_elements:
        print(number)




