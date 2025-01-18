# all this code is not working corectlly according the condition of the task.
# first approach
# # number_1 = int(input())
# # number_2 = int(input())
# #
# # even_elements = 0
# # odd_elements = 0
# # equal_sum = 0
# #
# # for iteration in range(number_1, number_2 + 1):
# #     #for index_sum_check in range(iteration):
# #         # if index_sum_check % 2 == 0:
# #         #     even_elements += index_sum_check
# #         # elif index_sum_check % 2 != 0:
# #         #     odd_elements += index_sum_check
# #
# #     print(iteration)



# second approach
# number_1 = int(input())
# number_2 = int(input())
#
# even_elements = 0
# odd_elements = 0
#
# for iteration in range(number_1, number_2 + 1):
#     for index_of_iteration in range(iteration):
#         if index_of_iteration % 2 == 0:
#             even_elements += index_of_iteration
#         else:
#             odd_elements += index_of_iteration
#
# if even_elements == odd_elements:
#     print(number_1)
# else:
#     print('no match')




# for number in range(number_1, number_2 + 1):
#     for indexes in range(number):
#         if indexes % 2 == 0:
#             even_elements += indexes
#         else:
#             odd_elements += indexes
#
#     if even_elements == odd_elements:
#         print(number)
#

# text = 'Hello'
# for index, letter in enumerate(text):
#     print(f'The letter that is on {index} is {letter}')




# this is the teacher approach and is 100% working
# number_1 = int(input())
# number_2 = int(input())

# for number in range(number_1, number_2 + 1):
#     even_elements = 0
#     odd_elements = 0
#     for index, value in enumerate(str(number)):
#         if index % 2 == 0:
#             even_elements += int(value)
#         else:
#             odd_elements += int(value)
#
#     if even_elements == odd_elements:
#         print(number, end=' ')




# third approach
# Why is not working?
# number_1 = int(input())
# number_2 = int(input())
#
# for iteration in range(number_1, number_2 + 1):
#     even_elements = 0
#     odd_elements = 0
#
#     for index_of_iteration in (str(iteration)):
#         if int(index_of_iteration) % 2 == 0:
#             even_elements += int(index_of_iteration)
#         else:
#             odd_elements += int(index_of_iteration)
#
#     if even_elements == odd_elements:
#         print(f'{iteration}', end=' ')




# number_1 = int(input())
# number_2 = int(input())
#
# for iteration in range(number_1, number_2 + 1):
#     even_elements = 0
#     odd_elements = 0
#     digits = str(iteration)
#
#     for index in range(len(digits)):
#         value = int(digits[index])
#         if index % 2 == 0:  # Even index
#             even_elements += value
#         else:  # Odd index
#             odd_elements += value
#
#     if even_elements == odd_elements:
#         print(f'{iteration}', end=' ')

total_sum = 0

for iteration in range(1, 10 + 1):
    total_sum += iteration
print(total_sum)
