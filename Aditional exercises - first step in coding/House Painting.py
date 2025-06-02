high_of_walls = float(input())
length = float(input())
high_of_roof = float(input())

area_of_door = 1.2 * 2.0
area_of_windows = (1.5 * 1.5) * 2
GREEN_PAINT = 3.4
RED_PAINT = 4.3

total_area_short_walls = ((high_of_walls * high_of_walls) * 2) - area_of_door
area_of_long_wall = ((high_of_walls * length) * 2) - area_of_windows

area_of_roof1 = (high_of_walls * length) * 2
are_of_roof2 = (high_of_walls * high_of_roof / 2) * 2

total_area_walls = area_of_long_wall + total_area_short_walls
total_roof_area = area_of_roof1 + are_of_roof2

green_paint = total_area_walls / GREEN_PAINT
red_paint = total_roof_area / RED_PAINT

print("{:.2f}".format(green_paint))
print("{:.2f}".format(red_paint))