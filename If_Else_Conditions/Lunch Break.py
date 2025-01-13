#user data reading
movie_name = input()
movie_length = int(input())
rest_length = int(input())

import math
#how much is 1/8 from all the time.This is the time for eat.
time_for_eat = rest_length / 8

#How much is 1/4 from all the time.This is the time for rest.
time_for_rest = rest_length / 4

#calculating total time to do all.
total_time = time_for_rest + time_for_eat + movie_length

#The difference between both times
left_time = math.ceil(abs(total_time - rest_length))

#if-else check,the time you have is enough or not.
if total_time <= rest_length:
    print(f"You have enough time to watch {movie_name} and left with {left_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {left_time} more minutes.")
