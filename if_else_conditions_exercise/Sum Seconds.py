import math
first_player = int(input())
second_player = int(input())
third_player = int(input())

total_time = first_player + second_player + third_player
time_in_minutes = total_time // 60
time_in_seconds = total_time % 60

if time_in_seconds < 10:
    print(f'{math.floor(time_in_minutes)}:0{time_in_seconds}')
else:
    print(f'{math.floor(time_in_minutes)}:{time_in_seconds}')








