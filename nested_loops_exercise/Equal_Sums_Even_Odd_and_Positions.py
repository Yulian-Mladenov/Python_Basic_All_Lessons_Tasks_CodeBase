# number_1 = int(input())
# number_2 = int(input())
#
# even_elements = 0
# odd_elements = 0
# equal_sum = 0
#
# for iteration in range(number_1, number_2 + 1):
#     #for index_sum_check in range(iteration):
#         # if index_sum_check % 2 == 0:
#         #     even_elements += index_sum_check
#         # elif index_sum_check % 2 != 0:
#         #     odd_elements += index_sum_check
#
#     print(iteration)

number_1 = int(input())
number_2 = int(input())

even_elements = 0
odd_elements = 0

for iteration in range(number_1, number_2 + 1):
    for index_of_iteration in range(iteration):
        if index_of_iteration % 2 == 0:
            even_elements += index_of_iteration
        else:
            odd_elements += index_of_iteration

if even_elements == odd_elements:
    print(number_1)
else:
    print('no match')
    
for number in range(number_1, number_2 + 1):
    for indexes in range(number):
        if indexes % 2 == 0:
            even_elements += indexes
        else:
            odd_elements += indexes

    if even_elements == odd_elements:
        print(number)




>>>>>>> fa66391019a4bf44e9095fc165d5a44430fc4d94
