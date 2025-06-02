length = float(input())*100
high = float(input())*100

corridor = 100
length_of_one_working_place = 120
high_of_one_working_place = 70
missing_places = 3

columns_in_length = length // length_of_one_working_place
columns_in_high = (high - corridor) // high_of_one_working_place

total_places = (columns_in_high * columns_in_length) - missing_places

print("%2.f" % total_places)





# import math
# length = float(input())*100
# width = float(input())*100
#
# COLUM_LENGTH = 120
# COLUM_WIDTH = 70
# CORIDOR = 100
# MISS_PLACES = 3
#
# colums_in_width = (width - CORIDOR) // COLUM_WIDTH
# colums_in_length = length // COLUM_LENGTH
#
# total_places = (colums_in_length * colums_in_width) - MISS_PLACES
#
# print("%2.f" % total_places)



