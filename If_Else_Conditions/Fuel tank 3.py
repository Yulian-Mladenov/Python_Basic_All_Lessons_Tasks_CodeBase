# type_fuel = input()
# fuel_quantity = float(input())

# if type_fuel == "Gasoline":
#     if fuel_quantity >= 25:
#         print(f"You have enough {type_fuel}.")
# elif type_fuel == "Gas":
#     if fuel_quantity >= 25:
#         print(f"You have enough {type_fuel}.")
# elif type_fuel == "Diesel":
#     if fuel_quantity >= 25:
#         print(f"You have enough {type_fuel}.")
# elif type_fuel == "Gasoline":
#     if fuel_quantity < 25:
#         print(f"Fill your tank with {type_fuel}!")
# elif type_fuel == "Gas":
#     if fuel_quantity < 25:
#         print(f"Fill your tank with {type_fuel}!")
# elif type_fuel == "Diesel":
#     if fuel_quantity < 25:
#         print(f"Fill your tank with {type_fuel}!")
# elif type_fuel != "Gas":
#     print("Invalid fuel!")
# elif type_fuel != "Gasoline":
#     print("Invalid Fuel!")
# elif type_fuel != "Diesel":
#     print("Invalid fuel!")

# и двете решения не работят напълно,долното работи само с думата газ,а горното само с думата газолине.
type_of_fuel = input()
fuel_quantity_in_the_tank = float(input())

if fuel_quantity_in_the_tank >= 25:
    if type_of_fuel == "Diesel":
        print(f"You have enough {type_of_fuel}.")
elif fuel_quantity_in_the_tank >= 25:
    if type_of_fuel == "Diesel":
        print(f"You have enough {type_of_fuel}.")
elif fuel_quantity_in_the_tank >= 25:
    if type_of_fuel == "Gasoline":
        print(f"You have enough {type_of_fuel}.")
elif fuel_quantity_in_the_tank < 25:
    if type_of_fuel == "Diesel":
        print(f"Fill your tank with {type_of_fuel}!")
elif fuel_quantity_in_the_tank < 25:
    if type_of_fuel == "Gasoline":
        print(f"Fill your tank with {type_of_fuel}!")
elif fuel_quantity_in_the_tank < 25:
    if type_of_fuel == "Diesel":
        print(f"Fill your tank with {type_of_fuel}!")
else:
    print("Invalid fuel!")
