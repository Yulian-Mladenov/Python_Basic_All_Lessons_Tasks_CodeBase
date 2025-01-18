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
#
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
#
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
number_1 = int(input())
number_2 = int(input())
iteration_counter_in_first_loop = 0
iteration_counter_in_second_loop = 0

for iteration in range(number_1, number_2 + 1):
    even_elements = 0
    odd_elements = 0
    iteration_counter_in_first_loop += 1

    for index_of_iteration in range(iteration):
        iteration_counter_in_second_loop += 1
        if index_of_iteration % 2 == 0:
            even_elements += index_of_iteration
        else:
            odd_elements += index_of_iteration

    if even_elements == odd_elements:
        print(iteration)
