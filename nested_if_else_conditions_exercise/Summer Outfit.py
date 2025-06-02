# first approach
# degrees = int(input())
# time = input()
#
# outfit = ''
# shoes = ''
#
# if 10 <= degrees <= 18 and time == 'Morning':
#     outfit = 'Sweatshirt'
#     shoes = 'Sneakers'
# elif 10 <= degrees <= 18 and time == 'Afternoon':
#     outfit = 'Shirt'
#     shoes = 'Moccasins'
# elif 10 <= degrees <= 18 and time == 'Evening':
#     outfit = 'Shirt'
#     shoes = 'Moccasins'
# elif 18 < degrees <= 24 and time == 'Morning':
#     outfit = 'Shirt'
#     shoes = 'Moccasins'
# elif 18 < degrees <= 24 and time == 'Afternoon':
#     outfit = 'T-Shirt'
#     shoes = 'Sandals'
# elif 18 < degrees <= 24 and time == 'Evening':
#     outfit = 'Shirt'
#     shoes = 'Moccasins'
# elif degrees >= 25 and time == 'Morning':
#     outfit = "T-Shirt"
#     shoes = 'Sandals'
# elif degrees >= 25 and time == 'Afternoon':
#     outfit = 'Swim Suit'
#     shoes = 'Barefoot'
# elif degrees >= 25 and time == 'Evening':
#     outfit = 'Shirt'
#     shoes = 'Moccasins'
#
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
#
#
#



# second approach
degrees = int(input())
time = input()

outfit = ''
shoes = ''

if 10 <= degrees <= 18 and time == 'Morning':
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'

elif 10 <= degrees <= 18 and time == 'Afternoon' or 10 <= degrees <= 18 and time == 'Evening' or 18 < degrees <= 24 and time == 'Morning' or 18 < degrees <= 24 and time == 'Evening' or degrees >= 25 and time == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'

elif 18 < degrees <= 24 and time == 'Afternoon' or degrees >= 25 and time == 'Morning':
    outfit = 'T-Shirt'
    shoes = 'Sandals'

elif degrees >= 25 and time == 'Afternoon':
    outfit = 'Swim Suit'
    shoes = 'Barefoot'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")





# third approach
degrees = int(input())
time = input()
outfit = 0
shoes = 0

if time == "Morning":
    if 10 <= degrees <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 <= degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degrees >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"

elif time == "Afternoon":
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 <= degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif degrees >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"

elif time == "Evening":
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 <= degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= 25:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")


