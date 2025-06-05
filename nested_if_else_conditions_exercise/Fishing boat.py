# input data
budget = int(input())
season = input()
number_of_people = int(input())

# prices
summer_and_autumn_price = 4200
winter_price = 2600
spring_price = 3000

# discounts based on people quantity
till_six_and_included = 0.10
more_than_seven_till_eleven_included = 0.15
more_than_twelve = 0.25

# additional discount - without autumn and only if the number of people is even.
# This discount is added after the price is already discounted!
add_discount = 0.05

# logic
first_price = 0

if season == 'Spring':
    if number_of_people <= 6:
        first_price = spring_price - (spring_price * till_six_and_included)
    elif 7 <= number_of_people <= 11:
        first_price = spring_price - (spring_price * more_than_seven_till_eleven_included)
    elif number_of_people > 12:
        first_price = spring_price - (spring_price * more_than_twelve)

elif season == 'Summer':
    if number_of_people <= 6:
        first_price = summer_and_autumn_price - (summer_and_autumn_price * till_six_and_included)
    elif 7 <= number_of_people <= 11:
        first_price = summer_and_autumn_price - (summer_and_autumn_price * more_than_seven_till_eleven_included)
    elif number_of_people > 12:
        first_price = summer_and_autumn_price - (summer_and_autumn_price * more_than_twelve)

elif season == 'Autumn':
    if number_of_people <= 6:
        first_price = summer_and_autumn_price - (summer_and_autumn_price * till_six_and_included)
    elif 7 <= number_of_people <= 11:
        first_price = summer_and_autumn_price - (summer_and_autumn_price * more_than_seven_till_eleven_included)
    elif number_of_people > 12:
        first_price = summer_and_autumn_price - (summer_and_autumn_price * more_than_twelve)

elif season == 'Winter':
    if number_of_people <= 6:
        first_price = winter_price - (winter_price * till_six_and_included)
    elif 7 <= number_of_people <= 11:
        first_price = winter_price - (winter_price * more_than_seven_till_eleven_included)
    elif number_of_people > 12:
        first_price = winter_price - (winter_price * more_than_twelve)

if season == 'Spring' or season == 'Winter' or season == 'Summer' and number_of_people % 2 == 0:
    first_price -= first_price * 0.05


# final result
if budget >= first_price:
    print(f"Yes! You have {budget - first_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {first_price - budget:.2f} leva.")

# this code not return 100/100 points. There is an issue in line 55. Why and what is the issue?
