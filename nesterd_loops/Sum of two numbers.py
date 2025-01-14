# this code is working, but it print all combinations which are matching with the magical number, not only the first matching combination.
begging_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())

counter = 0

for index_1 in range(begging_of_interval, end_of_interval + 1):
    for index_2 in range(begging_of_interval, end_of_interval + 1):
        counter += 1
        if index_1 + index_2 == magic_number:
            print(f'Combination N: {counter} ({index_1} + {index_2} = {magic_number})')
            break

else:
    print(f"{counter} combinations - neither equals {magic_number}")


# this code is working also, but is printing only the first matching number. In the condition is not written in detail that, so is tricky.
# starting_number = int(input())
# final_number = int(input())
# magic_number = int(input())
#
# combinations = 0
# is_found = False
# for i in range(starting_number, final_number + 1):
#     for j in range(starting_number, final_number + 1):
#         combinations += 1
#         if i + j == magic_number:
#             print(f"Combination N:{combinations} ({i} + {j} = {magic_number})")
#             is_found = True
#             break
#     if is_found:
#         break

# on line 31 this statement is necessery to break the first for loop, otherwise the code will count all combinations
# equal to the magic number. In the condition of the task is not written, but the program must stop when the first
# combination is find. Is written.
# So to stop the code after the first matching combination is found, must stop the first for loop also, otherwise
# he will start to count again, because only the second for loop is stoped.

# if i + j != magic_number:
#     print(f"{combinations} combinations - neither equals {magic_number}")