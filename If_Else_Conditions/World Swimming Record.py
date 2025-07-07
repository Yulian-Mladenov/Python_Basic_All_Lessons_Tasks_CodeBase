record_in_seconds = float(input())
distance_in_meters = float(input())
time_to_reach_one_meter = float(input()) #this time is in seconds

time_in_plus = 12.5
each_meters_more_seconds = 15

total_time = time_to_reach_one_meter * distance_in_meters

import math
times_slow_down = math.floor(distance_in_meters / each_meters_more_seconds) * time_in_plus

real_time = total_time + times_slow_down
real_time_2 = real_time - record_in_seconds

if real_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {real_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {real_time_2:.2f} seconds slower.")










