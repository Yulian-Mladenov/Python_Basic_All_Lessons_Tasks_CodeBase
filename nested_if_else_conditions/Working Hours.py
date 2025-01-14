# aproach 1
# hour = int(input())
# day_of_week = input()
#
# if day_of_week == "Monday" and 10 <= hour <= 18:
#     print("open")
# elif day_of_week == "Tuesday" and 10 <= hour <= 18:
#     print("open")
# elif day_of_week == "Wednesday" and 10 <= hour <= 18:
#     print("open")
# elif day_of_week == "Thursday" and 10 <= hour <= 18:
#     print("open")
# elif day_of_week == "Friday" and 10 <= hour <= 18:
#     print("open")
# elif day_of_week == "Saturday" and 10 <= hour <= 18:
#     print("open")
# else:
#     print("closed")


# approach 2
# hour = int(input())
# day_of_week = input()
#
# if 10 <= hour <= 18 and day_of_week == "Monday" or day_of_week == "Tuesday":
#     print("open")
# elif 10 <= hour <= 18 and day_of_week == "Wednesday" or day_of_week == "Thursday":
#     print("open")
# elif 10 <= hour <= 18 and day_of_week == "Friday" or day_of_week == "Saturday":
#     print("open")
# else:
#     print("closed")


# that will not work corecctly,it will print all three results at the same time
# hour = int(input())
# day_of_week = input()
#
# print("open") if 10 <= hour <= 18 and day_of_week == "Monday" or day_of_week == "Tuesday" else print("closed")
# print("open") if 10 <= hour <= 18 and day_of_week == "Wednesday" or day_of_week == "Thursday" else print("closed")
# print("open") if 10 <= hour <= 18 and day_of_week == "Friday" or day_of_week == "Saturday" else print("closed")

#this threee approaches will never working fully correct.Try with different day and differetn hours and see.
#It will never work correct because if just one of the results is folse will print open.
#and if write 19 monday will print open but actually is not true.
# hour = int(input())
# day_of_week = input()
#
# if hour < 10 or hour > 18 and day_of_week == "Sunday":
#     print("closed")
# else:
#     print("open")

# hour = int(input())
# day_of_week = input()
#
# if hour < 10 or hour > 18 and day_of_week == "Sunday":
#     print("closed")
# else:
#     print("open")

# hour = int(input())
# day_of_week = input()
#
# if (hour < 10 or hour > 18) and day_of_week == "Sunday":
#     print("closed")
# else:
#     print("open")


#this approach also will work all the time
# hour = int(input())
# day_of_week = input()
# #
# if hour >= 10 and hour <= 18:
#     if day_of_week != "Sunday":
#         print("open")
#     else:
#         print("closed")
# else:
#     print("closed")

#this approach will work all the time.
# hour = int(input())
# day_of_week = input()
#
# if 10 <= hour <= 18:
#     if day_of_week == "Sunday":
#         print("closed")
#     else:
#         print("open")
# else:
#     print("closed")


#sugar syntax approach
# hour = int(input())
# day_of_week = input()
#
# print('open') if 10 <= hour <= 18 and day_of_week != "Sunday" else print("closed")


