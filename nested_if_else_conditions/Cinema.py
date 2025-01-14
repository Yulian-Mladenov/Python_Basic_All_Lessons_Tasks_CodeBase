#1-st approach
# screening = input()
# columns = int(input())
# lines = int(input())
#
# total_sum = 0
#
# if screening == "Premiere":
#     Premiere = 12.00
#     total_sum = Premiere * (columns * lines)
# elif screening == "Normal":
#     Normal = 7.50
#     total_sum = Normal * (columns * lines)
# elif screening == "Discount":
#     Discount = 5.00
#     total_sum = Discount * (columns * lines)
#
# print(f"{total_sum:.2f} leva")

#2-nd approach
# screening = input()
# columns = int(input())
# lines = int(input())
#
# income = 0
# cinema_capacity = columns * lines
#
# if screening == "Premiere":
#     income = cinema_capacity * 12.00
# elif screening == "Normal":
#     income = cinema_capacity * 7.50
# elif  screening == "Discount":
#     income = cinema_capacity * 5.00
#
# print(f"{income:.2f} leva")

#3-th approach
screening = input()
columns = int(input())
lines = int(input())

income = 0

if screening == "Premiere":
    income = (columns * lines) * 12.00
elif screening == "Normal":
    income = (columns * lines) * 7.50
elif screening == "Discount":
    income = (columns * lines) * 5.00

print(f"{income:.2f} leva")