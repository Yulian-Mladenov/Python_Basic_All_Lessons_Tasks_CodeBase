#user data reading
fuel_type = input()
fuel_quantity = float(input())
discount_card = input()

#constant data for calculations
gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
gasoline_discount = 0.18 * fuel_quantity
diesel_discount = 0.12 * fuel_quantity
gas_discount = 0.08 * fuel_quantity

#fuel price according to fuel type.
if fuel_type == "Gas":
    total_fuel_price = fuel_quantity * gas_price
elif fuel_type == "Gasoline":
    total_fuel_price = fuel_quantity * gasoline_price
elif fuel_type == "Diesel":
    total_fuel_price = fuel_quantity * diesel_price

#fuel price according to dicount card
if discount_card == "Yes" and fuel_type == "Gas":
    total_fuel_price = total_fuel_price - gas_discount
elif discount_card == "Yes" and fuel_type == "Gasoline":
    total_fuel_price = total_fuel_price - gasoline_discount
elif discount_card == "Yes" and fuel_type == "Diesel":
    total_fuel_price = total_fuel_price - diesel_discount
else:
    total_fuel_price = total_fuel_price

#discount according quantity
fuel_discount_according_quantity_1 = total_fuel_price * 0.08
fuel_discount_according_quantity_2 = total_fuel_price * 0.10

#fuel price according quantity
if 20 <= fuel_quantity <= 25:
    total_fuel_price = total_fuel_price - fuel_discount_according_quantity_1
elif fuel_quantity > 25:
    total_fuel_price = total_fuel_price - fuel_discount_according_quantity_2
else:
    total_fuel_price = total_fuel_price

#print total result
print(f"{total_fuel_price:.2f} lv.")