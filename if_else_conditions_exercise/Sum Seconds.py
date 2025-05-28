import math
first_player = int(input())
second_player = int(input())
third_player = int(input())

total_time = first_player + second_player + third_player
time_in_minutes = 0
seconds = 0

if total_time > 59:
    time_in_minutes += 1
    seconds = total_time % 60

print(f'{time_in_minutes}:{seconds}')








