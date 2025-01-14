# degrees = int(input())
# time = input()
#
# if time == 'Morning' and 10 <= degrees <= 18:
#     print("Outfit = Sweatshirt \n Shoes = Sneakers")
# elif time == 'Afternoon' and 10 <= degrees <= 18:
#     print("Outfit = Shirt \n Shoes = Moccasins")
# elif time == 'Evening' and 10 <= degrees <= 18:
#     print("Outfit = Shirt \n Shoes = Moccasins")


# degrees = int(input())
# time = input()
#
# if time == "Morning":
#     if 10 <= degrees <= 18:
#         print("Outfit = Sweatshirt \n Shoes = Sneakers")
#     elif 18 <= degrees <= 24:
#         print("Outfit = Shirt \n Shoes = Moccasins")
#     elif degrees >= 25:
#         print("Outfit = T-Shirt \n Shoes = Sandals")
#
# elif time == "Afternoon":
#     if 10 <= degrees <= 18:
#         print("Outfit = Shirt \n Shoes = Moccasins")
#     elif 18 <= degrees <= 24:
#         print("Outfit = T-Shirt \n Shoes = Sandals")
#     elif degrees >= 25:
#         print("Outfit = Swim Suit \n Shoes = Barefoot")
#
#
# elif time == "Evening":
#     if 10 <= degrees <= 18:
#         print("Outfit = Shirt \n Shoes = Moccasins")
#     elif 18 <= degrees <= 24:
#         print("Outfit = Shirt \n Shoes = Moccasins")
#     elif degrees >= 25:
#         print("Outfit = Shirt \n Shoes = Moccasins")


#this solution is 100% working
# degrees = int(input())
# time = input()
# outfit = 0
# shoes = 0
#
# if time == "Morning":
#     if 10 <= degrees <= 18:
#         outfit = 'Sweatshirt'
#         shoes = 'Sneakers'
#     elif 18 <= degrees <= 24:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif degrees >= 25:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#
# elif time == "Afternoon":
#     if 10 <= degrees <= 18:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif 18 <= degrees <= 24:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#     elif degrees >= 25:
#         outfit = "Swim Suit"
#         shoes = "Barefoot"
#
# elif time == "Evening":
#     if 10 <= degrees <= 18:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif 18 <= degrees <= 24:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif degrees >= 25:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")


#this solution is working only on 60%
# degrees = int(input())
# time = input()
# outfit = 0
# shoes = 0
#
# if time == "Morning":
#     if 10 <= degrees <= 18:
#         outfit = 'Sweatshirt'
#         shoes = 'Sneakers'
#
# elif (time == "Morning" or time == "Evening") and (18 <= degrees <= 24):
#     outfit = "Shirt"
#     shoes = "Moccasins"
#
# elif time == "Morning":
#     if degrees >= 25:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#
# elif time == ("Afternoon" or time == "Evening") and (10 <= degrees <= 18):
#     outfit = 'Shirt'
#     shoes = 'Moccasins'
#
# elif time == "Afternoon":
#     if 18 <= degrees <= 24:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#     elif degrees >= 25:
#         outfit = "Swim Suit"
#         shoes = "Barefoot"
#
# elif time == "Evening":
#     if degrees >= 25:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
