covering_nylon_price_per_sq_meter = 1.50
paint_price_per_liter = 14.50
thinner_for_the_paint_price_per_liter = 5.00

add_paint_percentage = 0.10
add_cover_in_sq_meter = 2
bags = 0.40

necessary_cover_nylon = int(input())
necessary_quantity_paint_in_liters = int(input())
necessary_liters_thinner = int(input())
total_work_hours_necessary_to_be_done = int(input())

total_nylon_price = (necessary_cover_nylon * covering_nylon_price_per_sq_meter) + (add_cover_in_sq_meter * covering_nylon_price_per_sq_meter)
total_paint_quantity = (necessary_quantity_paint_in_liters * add_paint_percentage) + necessary_quantity_paint_in_liters
total_paint_price = total_paint_quantity * paint_price_per_liter
total_thinner_price = necessary_liters_thinner * thinner_for_the_paint_price_per_liter
total_material_price = total_thinner_price + total_paint_price + total_nylon_price + bags

price_for_painters_for_one_hour = total_material_price * 0.30
total_price_for_painters = price_for_painters_for_one_hour * total_work_hours_necessary_to_be_done

final_price_for_all = total_price_for_painters + total_material_price

print(f'{final_price_for_all}')





