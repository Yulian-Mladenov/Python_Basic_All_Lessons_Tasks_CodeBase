#this approach also is not working with edge number 99,because <=200 return true but 100<= return false
#auromaticly all is false and return invalid.
# number = int(input())
#
# if 100 <= number <= 200:
#     print("is valid")
# elif number == 0:
#     print("is valid")
# else:
#     print("invalid")

#this code is not working corecctly with number 99 because
# or is on the same line with and operator
# number = int(input())
#
# if 100 <= number <= 200 or number == 0:
#     print("is valid")
# else:
#     print("invalid")

#this approach is working
# number = int(input())
#
# valid = (100 <= number <= 200) or number == 0
#
# if not valid:
#     print("invalid")

#this approach is working also
# number = int(input())
#
# valid = 100 <= number <= 200 or number == 0
# else:
#     print("invalid")

#this is teaching example
# number = int(input())
#
# a = 10 > number
#
# print(a)

number = int(input())
valid = 100 <= number <= 200 or number == 0
if not valid:
    print("Invalid")
















