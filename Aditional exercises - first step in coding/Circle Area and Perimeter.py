radius = float(input())
import math

area_of_circle = (radius * radius) * math.pi
perimeter_of_circle = 2 * math.pi * radius

print("{:.2f}".format(area_of_circle))
print("{:.2f}".format(perimeter_of_circle))