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

# A bit of how the logic of this code is working. important - How the second for loop concatenate all even divisible
# digits? He not concatenate them! The if-else statements are checking first if the digit is zero: the variable
# magic_number remain False and then the execution only of the second for loop will be stopped, because the break
# command is only in his scope. Is useless to try to divide on zero, because on zero cannot be divide nothing it will
# return the same number. So automatically break and turn back to iterate another number.

# Then next case elif: If the digit is even divisible by zero, it means that this digit is a magic digit. And in this
# way checking digit by digit if each digit is even divisible till the last one included, it means that you check all
# digits one by one, that they are even divisible. When one by one each digit has a True value and also the value of
# the last digit is True, it means that all the number(all digits) is True, so the number is magic.

# Then you are asking else: In any other case, set up the value of magic_number on False.

# At the end you ask, if the variable magic_number is True print me the current number.

# The code do not concatenate the digits or collect them each by each to print them together at the end if the number
# is magic! No. The loop simple is checking if each digit is even divisible or not. Then you have to remember that
# till now all are even divisible so the magic_number is True, If all are even divisible so print the current number,
# if even one is not, so do not print this number. Practically the loop is checking digit by digit is the number
# magic or not. We can explain it with percentage example. 4 digit = 100%, so each digit is 25%. On each iteration we
# are covering 25% from the number. So on some iteration if the value of the digit is not even divisible on the
# number it means that this digit is not covering his 25% from the job, so automatically all process stop because is
# useless to check the rest of the digits if one of them cannot cover his own 25%. And that means this number is not
# magic. This process save a  lot of time for processing the code. So till the code is running trough the digits of
# one number it means that each previous digit is even divisible and the magic_number is settle to True. Also at the
# end, if all digits are even divisible so it means that after each check the value of magic_number is settle to
# True, and when the last digit also set up the magic_number on True it means that all the number is magical.

number = int(input())
magic_number = False

for special_number in range(1111, 10000):
    parsing_to_str = str(special_number)
    for string_number in parsing_to_str:
        if int(string_number) == 0:
            magic_number = False
            break
        elif number % int(string_number) == 0:
            magic_number = True
        else:
            magic_number = False
            break

    if magic_number is True:
        print(special_number, end=" ")

# Този код с флагови променливи учи как да изградиш крайния резултат без да използваш аритметика. Събиране,
# изваждане и т.н. Само с флагови променливи като превключватели събираш резултата и го изграждаш напълно.




# I wanted to see if i optimize the code eliminating those line down below it the code will work or not. It turn out
# that is not working. It`s printing sequential numbers not only the magical. In this configuration the code is not
# Not working correctly. Is printing many numbers which are sequential, not magical !

number = int(input())
magic_number = False

for special_number in range(1111, 10000):
    parsing_to_str = str(special_number)
    for string_number in parsing_to_str:
        if int(string_number) == 0:
            # magic_number = False
            break
        elif number % int(string_number) == 0:
            magic_number = True
        # else:
        #     magic_number = False
        #     break

    if magic_number is True:
        print(special_number, end=" ")

# This code is printing all number in sequence. Is because after once the flag variable is settle to True,
# the value remain True for all the rest of the digits, because no one of the other conditions can change the values
# to False to evade a printing of the current number.

# If come a digit not even divisible on zero the code automatically go on the bottom and execute the last two line.
# The first line contain condition if magic_number is true print the number. And is true because the previous digit
# was even divisible and set up the value of hte magic_number on True. Because there is no alternative to say stop, do
# not execute and print this number. That`s why is the last case else, to switch the value of magic_number on False
# and doing that stop the printing of the current number. Try with number 1117 with debugger and see what`s happen.
# Also eliminating line 81 it will have the same effect.

# Practically when you debug 1117 with initial number 3 for example what happen. First iterate 1,
# it setup magic_number value on True, because 3 % 1 return 3 without real number remaining, is even divide. So that
# setup magic_number on True. Then all that is repeated because next two digits are also 1. Then it come 7,
# NOT even divisible on 3, remain 1.4565...., so this case will not setup magic_number on True, because is not even
# divisible. So IDE is continue to executing the code, magic_number is already settle on True from the previous digit
# and the next lines for executing are to the check the value of magic_number and print the current number in the
# loop is the value of magic_number is True. And that will happen of course. But why?

# Because there is nothing to stop this action. There is no more condition in the scope of the nested for loop which
# can setup the value of magic_number on False to evade printing the number in the for loop when some of the digits
# is not even divisible. That`s why it will execute the print function and it will print the number which is not magic.
# All that explanation is according lines 85, 86, 87.

# Other test-case where the code it will not work correctly is the zero digit at the end of some number. For example
# 1120. It very depend from the input number, for example if we input 3 again, on number 1120 it will broke on digit
# 2. But if we input number 2, the code will broke on digit 0. The first two ones 1, 1 will setup the magic_number on
# True which is correct. Digit 2 also will be  correct, because is divisible even on 2. But the last digit 0 will
# break the execution of the for loop and because is the last digit, the IDE will return to the main scope and
# execute the last two lines of code. The value of magic_number will be True because the last digit 2 set it to True
# and that will print the current number which will be not magical. So again not magical numbers will be execute
# because there is nothing to stop their execution on the display. That why is necessary to write cases for each
# situation, to manage the condition of the flag variable because based on his value, the logic execute the code.
