import math
movie_name = input()
movie_duration = int(input())
break_duration = int(input())

time_for_lunch = break_duration / 8
time_for_rest = break_duration / 4

total_time_remain = break_duration - (time_for_rest + time_for_lunch)

time_difference = math.ceil(abs(total_time_remain - movie_duration))

if total_time_remain >= movie_duration:
    print(f"You have enough time to watch {movie_name} and left with {time_difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {time_difference} more minutes.")