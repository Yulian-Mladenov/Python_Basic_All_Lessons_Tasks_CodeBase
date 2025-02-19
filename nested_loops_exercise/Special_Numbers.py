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

magic_number = False

for special_number in range(1111, 10000):
    parsing_to_str = str(special_number)
    for string_number in parsing_to_str:
        if int(string_number) == 0:
            magic_number_is_found = True
            break
        elif number % int(string_number) == 0:
            magic_number = False
            break
        elif number % int(string_number) == 0:
            magic_number = True
        else:
            magic_number = False
            break

    if magic_number:
        print(special_number, end=" ")

# important - How the second for loop concatenate all even divisible digits? He not concatenate them! The if-else
# statements are checking first if the digit is zero it break the execution of the code. Is useless because on zero
# cannot be divide nothing. So automatically break and turn back to iterate another number. But if the digit is even
# divisible on zero, it means that this digit is a magic digit. And in this way checking digit by digit if each digit
# is even divisible till the last one included, it means that you check all digits one by one, that they are even
# divisible. When one by one each digit has a True value and also the value of the last digit is True, it means that
# all the number(all digits) are True, so the number is magic. So it means that all this number is magic. At the end
# you ask, if the variable magic_number is True print me the current number. The code do not concatenate the digits
# or collect them each by each to print them together at the end. No. The loop simple is checking if each digit is
# even divisible or not. If all=yes so print the current number, if even one no so do not print this number.
# Practically the loop is checking digit by digit is the number magic or not. We can explain it with percentage
# example. 4 digit = 100%, so each digit is 25%. On each iteration we are covering 25% from the number. So on some
# iteration if the value of the digit is not even divisible on the number it means that this digit is not covering
# his 25% from the job, so automatically all process stop because is useless to check the rest of the digits if one
# of them cannot cover his own 25%.

# Този код с флагови променливи учи как да изградиш крайния резултат без да използваш аритметика. Събиране, изваждане и т.н.
# Само с флагови променливи като превключватели събираш резултата и го изграждаш напълно.
