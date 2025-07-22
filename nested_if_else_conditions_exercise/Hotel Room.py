# input data:
month = input()
number_of_the_nights = int(input())

# studio prices for May and October:
studio_price_MO = 50
apartment_price_MO = 65

# studio prices for June and September:
studio_price_JS = 75.20
apartment_price_JS = 68.70

# studio prices for July and August:
studio_price_JA = 76
apartment_price_JA = 77

# discounts for studio for May and October for over 7 nights:
discount_MO_over_7 = 0.05
discount_MO_over_14 = 0.30

# discount for studio for June and September:
discount_JS_over_14 = 0.20

# discount for apartment, is regardless the month, only the nights number
apartment_discount_over_14 = 0.10

# prices variables:
studio_price = 0
apartment_price = 0

# the logic:
if month == 'May' or month == 'October':
    studio_price = studio_price_MO * number_of_the_nights
    apartment_price = apartment_price_MO * number_of_the_nights
    if number_of_the_nights > 14:
        studio_price -= studio_price * discount_MO_over_14
        apartment_price -= apartment_price * apartment_discount_over_14
    elif number_of_the_nights > 7:
        studio_price -= studio_price * discount_MO_over_7

elif month == 'June' or month == 'September':
    studio_price = studio_price_JS * number_of_the_nights
    apartment_price = apartment_price_JS * number_of_the_nights
    if number_of_the_nights > 14:
        studio_price -= studio_price * discount_JS_over_14
        apartment_price -= apartment_price_JS * apartment_discount_over_14

if month == 'July' or month == 'August':
    studio_price = studio_price_JA * number_of_the_nights
    apartment_price = apartment_price_JA * number_of_the_nights
    if number_of_the_nights > 14:
        apartment_price -= apartment_price * apartment_discount_over_14

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")



