# this is working with any case
# fruit = input()
# day_of_week = input()
# quantity = float(input())
#
# #prices on weekend
# banana_1 = 2.70
# apple_1 = 1.25
# orange_1 = 0.90
# grapefruit_1 = 1.60
# kiwi_1 = 3.00
# pineapple_1 = 5.60
# grapes_1 = 4.20
#
# #prices on working days
# banana = 2.50
# apple = 1.20
# orange = 0.85
# grapefruit = 1.45
# kiwi = 2.70
# pineapple = 5.50
# grapes = 3.85
#
# total_price = None
#
# if day_of_week == "Sunday" or day_of_week == "Saturday":
#     if fruit == "banana":
#         total_price = banana_1 * quantity
#         print(f"{total_price:.2f}")
#     elif fruit == "apple":
#         total_price = apple_1 * quantity
#         print(f"{total_price:.2f}")
#     elif fruit == "orange":
#         total_price = orange_1 * quantity
#         print(f"{total_price:.2f}")
#     elif fruit == "grapefruit":
#         total_price = grapefruit_1 * quantity
#         print(f"{total_price:.2f}")
#     elif fruit == "kiwi":
#         total_price = kiwi_1 * quantity
#         print(f"{total_price:.2f}")
#     elif fruit == "pineapple":
#         total_price = pineapple_1 * quantity
#         print(f"{total_price:.2f}")
#     elif fruit == "grapes":
#         total_price = grapes_1 * quantity
#         print(f"{total_price:.2f}")
#     else:
#         print("error")
#
# elif day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or\
#         day_of_week == "Thursday" or day_of_week == "Friday":
#     if fruit == "banana":
#         total_price = banana * quantity
#         print(f"{total_price:.2f}")
#     elif fruit == "apple":
#         total_price = apple * quantity
#         print(f"{total_price:.2f}")
#     elif fruit == "orange":
#         total_price = orange * quantity
#         print(f"{total_price:.2f}")
#     elif fruit == "grapefruit":
#         total_price = grapefruit * quantity
#         print(f"{total_price:.2f}")
#     elif fruit == "kiwi":
#         total_price = kiwi * quantity
#         print(f"{total_price:.2f}")
#     elif fruit == "pineapple":
#         total_price = pineapple * quantity
#         print(f"{total_price:.2f}")
#     elif fruit == "grapes":
#         total_price = grapes * quantity
#         print(f"{total_price:.2f}")
#     else:
#         print("error")
#
# else:
#     print("error")


# this is not working if the fruit name is wrong
import time
start_time = time.time()

fruit = input()
day_of_week = input()
quantity = float(input())


if day_of_week == "Sunday" or day_of_week == "Saturday":
    if fruit == "banana":
        banana_1 = 2.70
        total_price = banana_1 * quantity
    elif fruit == "apple":
        apple_1 = 1.25
        total_price = apple_1 * quantity
    elif fruit == "orange":
        orange_1 = 0.90
        total_price = orange_1 * quantity
    elif fruit == "grapefruit":
        grapefruit_1 = 1.60
        total_price = grapefruit_1 * quantity
    elif fruit == "kiwi":
        kiwi_1 = 3.00
        total_price = kiwi_1 * quantity
    elif fruit == "pineapple":
        pineapple_1 = 5.60
        total_price = pineapple_1 * quantity
    elif fruit == "grapes":
        grapes_1 = 4.20
        total_price = grapes_1 * quantity
    print(f"{total_price:.2f}")

elif day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or\
        day_of_week == "Thursday" or day_of_week == "Friday":
    if fruit == "banana":
        banana = 2.50
        total_price = banana * quantity
    elif fruit == "apple":
        apple = 1.20
        total_price = apple * quantity
    elif fruit == "orange":
        orange = 0.85
        total_price = orange * quantity
    elif fruit == "grapefruit":
        grapefruit = 1.45
        total_price = grapefruit * quantity
    elif fruit == "kiwi":
        kiwi = 2.70
        total_price = kiwi * quantity
    elif fruit == "pineapple":
        pineapple = 5.50
        total_price = pineapple * quantity
    elif fruit == "grapes":
        grapes = 3.85
        total_price = grapes * quantity
    print(f"{total_price:.2f}")

else:
    print("error")

print(total_price)

print("time elapsed: {:.2f}s".format(time.time() - start_time))


#this code is working in any case
# import time
#
# start_time = time.time()
#
# fruit = input()
# day_of_week = input()
# quantity = float(input())

# price = None
#
# if day_of_week == "Sunday" or day_of_week == "Saturday":
#     if fruit == "banana":
#         price = 2.70
#     elif fruit == "apple":
#         price = 1.25
#     elif fruit == "orange":
#         price = 0.90
#     elif fruit == "grapefruit":
#         price = 1.60
#     elif fruit == "kiwi":
#         price = 3.00
#     elif fruit == "pineapple":
#         price = 5.60
#     elif fruit == "grapes":
#         price = 4.20
#
# elif day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or \
#         day_of_week == "Thursday" or day_of_week == "Friday":
#     if fruit == "banana":
#         price = 2.50
#     elif fruit == "apple":
#         price = 1.20
#     elif fruit == "orange":
#         price = 0.85
#     elif fruit == "grapefruit":
#         price = 1.45
#     elif fruit == "kiwi":
#         price = 2.70
#     elif fruit == "pineapple":
#         price = 5.50
#     elif fruit == "grapes":
#         price = 3.85
#
#
# if price is None:
#     print("error")
# else:
#     price *= quantity
#     print(f"{price:.2f}")
#
# print("time elapsed: {:.2f}s".format(time.time() - start_time))
