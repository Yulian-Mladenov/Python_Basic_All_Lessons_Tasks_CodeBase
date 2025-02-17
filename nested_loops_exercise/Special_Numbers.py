number = int(input())
concatenation =

for special_number in range(1111, 10000):
    parsing_to_str = special_number # parsing the number to str data type
    for string_number in range(parsing_to_str):
        str_to_int = int(string_number) # parsing again each element from string to integer
        if str_to_int == 0:
            break
        elif number % str_to_int == 0:
            concatenation =