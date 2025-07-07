type_of_fuel = input()
fuel_quantity_in_the_tank = float(input())

if fuel_quantity_in_the_tank >= 25 and type_of_fuel == "Gas":
    print(f"You have enough {type_of_fuel}.")
elif fuel_quantity_in_the_tank >= 25 and type_of_fuel == "Gasoline":
    print(f"You have enough {type_of_fuel}.")
elif fuel_quantity_in_the_tank >= 25 and type_of_fuel == "Diesel":
    print(f"You have enough {type_of_fuel}.")
elif fuel_quantity_in_the_tank < 25 and type_of_fuel == "Diesel":
    print(f"Fill your tank with {type_of_fuel}!")
elif fuel_quantity_in_the_tank < 25 and type_of_fuel == "Gasoline":
    print(f"Fill your tank with {type_of_fuel}!")
elif fuel_quantity_in_the_tank < 25 and type_of_fuel == "Gas":
    print(f"Fill your tank with {type_of_fuel}!")
else:
    print("Invalid fuel!")





