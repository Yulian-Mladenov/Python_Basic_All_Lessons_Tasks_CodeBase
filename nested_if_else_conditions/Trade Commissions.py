# this approach is not working with any case,because None cannot be multiply with float type data
# city = input()
# sells = float(input())
#
# commission = None
#
# if city == "Sofia" and 0 <= sells <= 500:
#     commission = 0.05
# elif city == "Sofia" and 500 <= sells <= 1000:
#     commission = 0.07
# elif city == "Sofia" and 1000 <= sells <= 10000:
#     commission = 0.08
# elif city == "Sofia" and sells > 10000:
#     commission = 0.12
#
# if city == "Varna" and 0 <= sells <= 500:
#     commission = 0.045 / 10
# elif city == "Varna" and 500 <= sells <= 1000:
#     commission = 0.75 / 10
# elif city == "Varna" and 1000 <= sells <= 10000:
#     commission = 0.10
# elif city == "Varna" and sells > 10000:
#     commission = 0.13
#
# if city == "Plovdiv" and 0 <= sells <= 500:
#     commission = 0.55 / 10
# elif city == "Plovdiv" and 500 <= sells <= 1000:
#     commission = 0.8
# elif city == "Plovdiv" and 1000 <= sells <= 10000:
#     commission = 0.12
# elif city == "Plovdiv" and sells > 10000:
#     commission = 0.145 / 10
#
# total_commission = commission * sells
#
# if commission is None:
#     print("error")
# else:
#     print(f"{total_commission:.2f}")


# this approach is working with any case
# city = input()
# sells = float(input())
#
# commission = 0
#
# if city == "Sofia" and 0 <= sells <= 500:
#     commission = 0.05
# elif city == "Sofia" and 500 <= sells <= 1000:
#     commission = 0.07
# elif city == "Sofia" and 1000 <= sells <= 10000:
#     commission = 0.08
# elif city == "Sofia" and sells > 10000:
#     commission = 0.12
#
# if city == "Varna" and 0 <= sells <= 500:
#     commission = 0.045
# elif city == "Varna" and 500 <= sells <= 1000:
#     commission = 0.075
# elif city == "Varna" and 1000 <= sells <= 10000:
#     commission = 0.10
# elif city == "Varna" and sells > 10000:
#     commission = 0.13
#
# if city == "Plovdiv" and 0 <= sells <= 500:
#     commission = 0.055
# elif city == "Plovdiv" and 500 <= sells <= 1000:
#     commission = 0.08
# elif city == "Plovdiv" and 1000 <= sells <= 10000:
#     commission = 0.12
# elif city == "Plovdiv" and sells > 10000:
#     commission = 0.145
#
# total_commission = commission * sells
#
# if commission <= 0:
#     print("error")
# else:
#     print(f"{total_commission:.2f}")


#this approach is wotking with any case
# city = input()
# sells = float(input())
#
# commission = 0
#
# if city == "Sofia":
#     if 0 <= sells <= 500:
#         commission = 0.05
#     elif 500 <= sells <= 1000:
#         commission = 0.07
#     elif 1000 <= sells <= 10000:
#         commission = 0.08
#     elif sells > 10000:
#         commission = 0.12
#
# elif city == "Varna":
#     if 0 <= sells <= 500:
#         commission = 0.045
#     elif 500 <= sells <= 1000:
#         commission = 0.075
#     elif 1000 <= sells <= 10000:
#         commission = 0.10
#     elif sells > 10000:
#         commission = 0.13
#
# elif city == "Plovdiv":
#     if 0 <= sells <= 500:
#         commission = 0.055
#     elif 500 <= sells <= 1000:
#         commission = 0.08
#     elif 1000 <= sells <= 10000:
#         commission = 0.12
#     elif sells > 10000:
#         commission = 0.145
#
# total_commission = commission * sells
#
# if commission <= 0:
#     print("error")
# else:
#     print(f"{total_commission:.2f}")
#
#
# #this approach is working in any case
# city = input()
# sells = float(input())
#
# if city == "Sofia":
#     if 0 <= sells <= 500:
#         commission = 0.05
#         print(f"{commission * sells:.2f}")
#     elif 500 <= sells <= 1000:
#         commission = 0.07
#         print(f"{commission * sells:.2f}")
#     elif 1000 <= sells <= 10000:
#         commission = 0.08
#         print(f"{commission * sells:.2f}")
#     elif sells > 10000:
#         commission = 0.12
#         print(f"{commission * sells:.2f}")
#     else:
#         print("error")
#
# elif city == "Varna":
#     if 0 <= sells <= 500:
#         commission = 0.045
#         print(f"{commission * sells:.2f}")
#     elif 500 <= sells <= 1000:
#         commission = 0.075
#         print(f"{commission * sells:.2f}")
#     elif 1000 <= sells <= 10000:
#         commission = 0.10
#         print(f"{commission * sells:.2f}")
#     elif sells > 10000:
#         commission = 0.13
#         print(f"{commission * sells:.2f}")
#     else:
#         print("error")
#
# elif city == "Plovdiv":
#     if 0 <= sells <= 500:
#         commission = 0.055
#         print(f"{commission * sells:.2f}")
#     elif 500 <= sells <= 1000:
#         commission = 0.08
#         print(f"{commission * sells:.2f}")
#     elif 1000 <= sells <= 10000:
#         commission = 0.12
#         print(f"{commission * sells:.2f}")
#     elif sells > 10000:
#         commission = 0.145
#         print(f"{commission * sells:.2f}")
#     else:
#         print("error")
#
# else:
#     print("error")


#this approach also is working with any case,but is sllower.
# city = input()
# sells = float(input())
#
# commission = 0
#
# if city == "Sofia":
#     if 0 <= sells <= 500: commission = 0.05
#     elif 500 <= sells <= 1000: commission = 0.07
#     elif 1000 <= sells <= 10000: commission = 0.08
#     elif sells > 10000: commission = 0.12
#
# elif city == "Varna":
#     if 0 <= sells <= 500: commission = 0.045
#     elif 500 <= sells <= 1000: commission = 0.075
#     elif 1000 <= sells <= 10000: commission = 0.10
#     elif sells > 10000: commission = 0.13
#
# elif city == "Plovdiv":
#     if 0 <= sells <= 500: commission = 0.055
#     elif 500 <= sells <= 1000: commission = 0.08
#     elif 1000 <= sells <= 10000: commission = 0.12
#     elif sells > 10000: commission = 0.145
#
# print("error") if commission <= 0 else print(f"{commission * sells:.2f}")

