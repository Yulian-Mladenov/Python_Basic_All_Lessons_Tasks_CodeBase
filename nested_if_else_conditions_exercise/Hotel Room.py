# input data:
month = input()
number_of_the_nights = int(input())

# prices according the month:
studio_price = 0
studio_discount = 0
apartment_price = 0
apartment_discount = 0
final_price_without_discount = month * number_of_the_nights
final_price_with_discount = month * number_of_the_nights

# if month == 'May' or month == 'October':
#     studio_price = 50
#     if number_of_the_nights > 14:
#         studio_discount = 0.30
#     elif number_of_the_nights > 7:
#         studio_discount = 0.05
#     apartment_price = 65
#     if number_of_the_nights > 14:
#         apartment_discount = 0.10

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65

elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70

elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

if number_of_the_nights > 14 and month == 'May' or month == 'October':


print(f"Apartment:{apartment_price * number_of_the_nights:.2f} lv.")
print(f"Studio: {studio_price * number_of_the_nights:.2f} lv.")



