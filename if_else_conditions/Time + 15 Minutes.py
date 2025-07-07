hours_1 = int(input())
minutes_1 = int(input()) + 15

if minutes_1 >= 60:
    hours_1 = hours_1 + 1
    minutes_1 = minutes_1 - 60

if hours_1 > 23:
     hours_1 = hours_1 - 24

if minutes_1 < 10:
    print(f'{hours_1}:0{minutes_1}')
else:
    print(f'{hours_1}:{minutes_1}')







