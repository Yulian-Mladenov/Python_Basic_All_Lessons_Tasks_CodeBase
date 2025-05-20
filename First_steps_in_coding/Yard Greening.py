square_meters_to_greening = float(input())

discount = 18
price_per_greening_one_square_meter_with_taxes = 7.61

total_amount = square_meters_to_greening * price_per_greening_one_square_meter_with_taxes
total_amount_with_discount = (total_amount * discount) / 100
discount_amount = total_amount - total_amount_with_discount

print(f"The discount is: {discount_amount} lv.")
print(f"The final price is: {total_amount_with_discount} lv.")

