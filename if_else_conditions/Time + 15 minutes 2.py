# hours = int(input())
# minutes = int(input())
#
# minutes_2 = minutes + 15
# hours_2 = hours
# if minutes_2 >= 60:
#     hours_2 = hours + 1
#     minutes_2 = minutes_2 - 60
#
# if hours_2 > 23:
#     hours_2 = hours_2 - 24
#
# if minutes_2 < 10:
#     print(f'{hours_2}:0{minutes_2}')
# else:
#     print(f'{hours_2}:{minutes_2}')
#
#

hours = int(input())
minutes = int(input())

hours_2 = hours
minutes_2 = minutes + 15

if minutes_2 >= 60:
    hours_2 = hours_2 + 1
    minutes_2 = minutes_2 - 60

result_hours = str(hours_2)
result_minutes = str(minutes_2)

if minutes_2 < 10:
    result_minutes = "0"+str(minutes_2)
if hours_2 >= 24:
    result_hours = str(hours_2 - 24)

print(f'{result_hours}:{result_minutes}')



