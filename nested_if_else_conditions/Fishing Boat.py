import time
start_time = time.time()

budget = int(input())
season = input()
group = int(input())

spring_boat_price = 3000
summer_boat_price = 4200
autumn_boat_price = 4200
winter_boat_price = 2600

discount = 0
price = 0

# here we are checking the season,the number of people and creating the initial discount value
if season == 'Summer' and group <= 6:
    discount = summer_boat_price * 0.10
    price = summer_boat_price - discount
elif season == 'Summer' and 7 <= group <= 11:
    discount = summer_boat_price * 0.15
    price = summer_boat_price - discount
elif season == 'Summer' and group > 12:
    discount = summer_boat_price * 0.25
    price = summer_boat_price - discount
elif season == 'Winter' and group <= 6:
    discount = winter_boat_price * 0.10
    price = winter_boat_price - discount
elif season == 'Winter' and 7 <= group <= 11:
    discount = winter_boat_price * 0.15
    price = winter_boat_price - discount
elif season == 'Winter' and group > 12:
    discount = winter_boat_price * 0.25
    price = winter_boat_price - discount
elif season == 'Spring' and group <= 6:
    discount = spring_boat_price * 0.10
    price = spring_boat_price - discount
elif season == 'Spring' and 7 <= group <= 11:
    discount = spring_boat_price * 0.15
    price = spring_boat_price - discount
elif season == 'Spring' and group > 12:
    discount = spring_boat_price * 0.25
    price = spring_boat_price - discount
elif season == 'Autumn' and group <= 6:
    discount = autumn_boat_price * 0.10
    price = autumn_boat_price - discount
elif season == 'Autumn' and 7 <= group <= 11:
    discount = autumn_boat_price * 0.15
    price = autumn_boat_price - discount
elif season == 'Autumn' and group > 12:
    discount = autumn_boat_price * 0.25
    price = autumn_boat_price - discount

# changing the price
if season == 'Spring' or season == 'Summer' or season == 'Winter':
    if group % 2 == 0:
        price = price - (price * 0.05)
    else:
        price = price

# calculating the difference
difference = abs(price - budget)

# checking the final result
if budget >= price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")

print("time elapsed: {:.2f}s".format(time.time() - start_time))


# import time
# start_time = time.time()
#
# budget = int(input())
# season = input()
# group = int(input())
#
# season_spring = "Spring"
# season_summer = "Summer"
# season_autumn_a = "Autumn"
# season_winter = "Winter"
#
# spring_boat_price = 3000
# summer_boat_price = 4200
# autumn_boat_price = 4200
# winter_boat_price = 2600
#
# discount_low = 6
# discount_middle_low_range = 7
# discount_middle_high_range = 11
# discount_high_range = 12
# discount_up_to_6 = 10 / 100
# discount_between_7_11 = 15 / 100
# discount_over_12 = 25 / 100
# discount_even = 5 / 100
#
# price = 0
#
# #creating of the price down below
# #filtration by season
# if season == season_spring:
#     price = spring_boat_price
# elif season == season_summer:
#     price = summer_boat_price
# elif season == season_autumn_a:
#     price = autumn_boat_price
# elif season == season_winter:
#     price = winter_boat_price
# else:
#     print("Invalid season")
#     exit()
#
# #filtration by number of people
# if group <= discount_low:
#     price -= price * discount_up_to_6
# elif discount_middle_low_range <= group <= discount_middle_high_range:
#     price -= price * discount_between_7_11
# elif group > discount_high_range:
#     price -= discount_over_12
#
# #filtration by season Autumn and even number of the people
# if season != season_autumn_a and group % 2 == 0:
#     price -= price * discount_even
#
# # # calculating the difference and final result
# if budget >= price:
#     difference = budget-price
#     print(f"Yes! You have {difference:.2f} leva left.")
# else:
#     difference = price - budget
#     print(f"Not enough money! You need {difference:.2f} leva.")
#
#
# print("time elapsed: {:.2f}s".format(time.time() - start_time))
