# my prototype
# number = int(input())
# concatenation =
#
# for special_number in range(1111, 10000):
#     parsing_to_str = str(special_number) # parsing the number to str data type
#     for string_number in parsing_to_str:
#         str_to_int = int(string_number) # parsing again each element from string to integer
#         if str_to_int == 0:
#             break
#         elif number % str_to_int == 0:
#             concatenation =

# here i stopped because it`s a moment to find out how to concatenate each element from the for loop in one string
# and when all are collected to parse them in integer again or print them directly like a string.



number = int(input())
magic_number_is_found = False


for special_number in range(1111, 10000):
    parsing_to_str = str(special_number) # parsing the number to str data type
    for string_number in parsing_to_str:
        if int(string_number) == 0:
            magic_number_is_found = True
            break
        elif number % str_to_int == 0:
