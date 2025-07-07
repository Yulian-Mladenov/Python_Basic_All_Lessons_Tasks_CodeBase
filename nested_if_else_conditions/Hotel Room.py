# month = input()
# days = int(input())
#
# m_a_o_p_s = 50
# m_a_o_p_a = 65
# s_a_j_p_s = 75.20
# s_a_j_p_a = 68.70
#
# total_price_for_studio= 0
# total_price_for_apartment = 0
# total_price = 0
# discount = 0
#
# if (month == "May" or month == "October") and 7 <=days <= 14:
#     total_price_for_studio = days * m_a_o_p_s
#     discount = total_price_for_studio - (total_price_for_studio * 0.05)
#     total_price = total_price_for_studio - discount
#     total_price_for_apartment = days * s_a_j_p_a
#     discount = total_price_for_apartment - (total_price_for_apartment * 0.10)
#     total_price = total_price_for_apartment - discount
#
#
# elif (month == "May" or month == "October") and days > 14:
#     total_price_for_studio = days * m_a_o_p_s
#     discount = total_price_for_studio - (total_price_for_studio * 0.30)
#     total_price = total_price_for_studio - discount
#     total_price_for_apartment = days * s_a_j_p_a
#     discount = total_price_for_apartment - (total_price_for_apartment * 0.10)
#     total_price = total_price_for_apartment - discount
#
# elif (month == "June" or month == "September") and days >= 14:
#     total_price_for_studio = days * s_a_j_p_s
#     discount = total_price_for_studio - (total_price_for_studio * 0.20)
#     total_price = total_price_for_studio - discount
#     total_price_for_apartment = days * s_a_j_p_a
#     discount = total_price_for_apartment - (total_price_for_apartment * 0.10)
#     total_price = total_price_for_apartment - discount
#
# elif days >= 14:
#     total_price_for_apartment = days * s_a_j_p_a
#     discount = total_price_for_apartment - (total_price_for_apartment * 0.10)
#     total_price = total_price_for_apartment - discount
#
# print(f"Apartment: {total_price_for_apartment:.2f} lv.")
#
# print(f"Studio: {total_price_for_studio:.2f} lv.")

# month = input()
# days = int(input())
#
# #constant data
# price_studio_october_may = 50
# price_apartment_october_may = 65
# price_studio_september_june = 75.20
# price_apartment_september_june = 68.70
#
# #discount for studio for may and october for more that 7 nights till 14
# discount_studio_may_october_1= 5 / 100
#
# #discount for studio for may and october for more than 14 nights
# discount_studio_may_october_2 = 30 / 100
#
# #discount for studio for september and june for more than 14 nights
# discount_studio_september_june = 20 / 100
#
# #diacount for apartment for more than 14 nights
# discount_apartment = 10 / 100
#
# final_price = 0
# total_price = 0
# discount = 0
#
# if month == "May" or month == "October":
# if 7 <= days <= 14:
# total_price = price_studio_october_may * days
# discount = total_price * 0.05
# total_price -= discount
# elif days > 14:
# total_price = price_studio_october_may * days
# discount = total_price * 0.30
# total_price -= discount
# else:
# total_price = price_studio_october_may * days
#
# elif month == "June" or month == "September":
# if days > 14:
# total_price = price_studio_september_june * days
# discount = total_price * 0.20
# total_price -= discount
# else:
# total_price = price_studio_september_june * days
#
# else:
# total_price
#
# print(f"{total_price:.2f}")


# month = input()
# number_of_nights = int(input())
#
# STUDIO_PRICE_MAY_OCTOBER = 50
# STUDIO_PRICE_JUNE_SEPTEMBER = 75.20
# STUDIO_PRICE_JULY_AUGUST = 76
#
# APARTMENT_PRICE_MAY_OCTOBER = 65
# APARTMENT_PRICE_JUNE_SEPTEMBER = 68.70
# APARTMENT_PRICE_JULY_AUGUST = 77
#
# studio_price = 0
# apartment_price = 0
# discount_studio = 0
# discount_apartment = 0
#
# if month == "May" or month == "October":
#     if 7 <= number_of_nights <= 14:
#         studio_price = STUDIO_PRICE_MAY_OCTOBER * number_of_nights
#         discount_studio = studio_price * 0.05
#         studio_price -= discount_studio
#         apartment_price = APARTMENT_PRICE_MAY_OCTOBER * number_of_nights
#     elif number_of_nights > 14:
#         studio_price = STUDIO_PRICE_MAY_OCTOBER * number_of_nights
#         discount = studio_price * 0.30
#         studio_price -= discount
#         apartment_price = APARTMENT_PRICE_MAY_OCTOBER * number_of_nights
#         discount_apartment = apartment_price * 0.10
#         apartment_price -= discount_apartment
#
# elif month == "June" or month == "September":
#     if 7 <= number_of_nights <= 14:
#         studio_price = STUDIO_PRICE_JUNE_SEPTEMBER * number_of_nights
#         apartment_price = APARTMENT_PRICE_JUNE_SEPTEMBER * number_of_nights
#     elif number_of_nights > 14:
#         studio_price = STUDIO_PRICE_JUNE_SEPTEMBER * number_of_nights
#         discount = studio_price * 0.20
#         studio_price -= discount
#         apartment_price = APARTMENT_PRICE_JUNE_SEPTEMBER * number_of_nights
#         discount_apartment = apartment_price * 0.10
#         apartment_price -= discount_apartment
#
# elif month == "July" or month == "August":
#     if 7 <= number_of_nights <= 14:
#         studio_price = STUDIO_PRICE_JULY_AUGUST * number_of_nights
#         apartment_price = APARTMENT_PRICE_JULY_AUGUST * number_of_nights
#     elif number_of_nights > 14:
#         studio_price = STUDIO_PRICE_JULY_AUGUST * number_of_nights
#         apartment_price = APARTMENT_PRICE_JULY_AUGUST * number_of_nights
#         discount_apartment = apartment_price * 0.10
#         apartment_price -= discount_apartment
#
# print(f"Apartment: {apartment_price:.2f} lv.")
# print(f"Studio: {studio_price:.2f} lv.")


month = input()
nights = int(input())

MONTH_MAY = "May"
MONTH_JUNE = "June"
MONTH_JULY = "July"
MONTH_AUGUST = "August"
MONTH_SEPTEMBER = "September"
MONTH_OCTOBER = "October"

STUDIO_PRICE_MAY_OCTOBER = 50
STUDIO_PRICE_JUNE_SEPTEMBER = 75.20
STUDIO_PRICE_JULY_AUGUST = 76

APARTMENT_PRICE_MAY_OCTOBER = 65
APARTMENT_PRICE_JUNE_SEPTEMBER = 68.70
APARTMENT_PRICE_JULY_AUGUST = 77

DISCOUNT_7_14_MAY_OCTOBER = 5 / 100
DISCOUNT_14_MAY_OCTOBER = 30 / 100
DISCOUNT_14_JUNE_SEPTEMBER = 20 / 100
DISCOUNT_APARTMENT = 10 / 100

STUDIO_LOW_NIGHTS_COUNT_MAY_OCTOBER = 7
STUDIO_HIGH_NIGHTS_COUNT_MAY_OCTOBER = 14
STUDIO_HIGH_NIGHTS_COUNT_JUNE_SEPTEMBER = 14
APARTMENT_NIGHTS_COUNT = 14

price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_studio = STUDIO_PRICE_MAY_OCTOBER * nights
    price_apartment = APARTMENT_PRICE_MAY_OCTOBER * nights
    if nights > STUDIO_HIGH_NIGHTS_COUNT_MAY_OCTOBER:
        price_studio -= price_studio * DISCOUNT_14_MAY_OCTOBER
        price_apartment -= price_apartment * DISCOUNT_APARTMENT
    elif nights > STUDIO_LOW_NIGHTS_COUNT_MAY_OCTOBER:
        price_studio -= price_studio * DISCOUNT_7_14_MAY_OCTOBER

elif month == "June" or month == "September":
    price_studio = STUDIO_PRICE_JUNE_SEPTEMBER * nights
    price_apartment = APARTMENT_PRICE_JUNE_SEPTEMBER * nights
    if nights > STUDIO_HIGH_NIGHTS_COUNT_JUNE_SEPTEMBER:
        price_studio -= price_studio * DISCOUNT_14_JUNE_SEPTEMBER
        price_apartment -= price_apartment * DISCOUNT_APARTMENT

elif month == "July" or month == "August":
    price_studio = STUDIO_PRICE_JULY_AUGUST* nights
    price_apartment = APARTMENT_PRICE_JULY_AUGUST * nights
    if nights > APARTMENT_NIGHTS_COUNT:
        price_apartment -= price_apartment * DISCOUNT_APARTMENT

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")




