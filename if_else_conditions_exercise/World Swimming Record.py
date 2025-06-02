record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_one_meter = float(input())

time_to_swim_the_distance = time_in_seconds_per_one_meter * distance_in_meters

additional_time = distance_in_meters // 15

time_to_swim_with_add_seconds = (additional_time * 12.5) + time_to_swim_the_distance

time_difference = time_to_swim_with_add_seconds - record_in_seconds

if time_to_swim_with_add_seconds < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {time_to_swim_with_add_seconds:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_difference:.2f} seconds slower.")


