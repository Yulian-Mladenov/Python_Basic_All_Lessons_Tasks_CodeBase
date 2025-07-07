# hour = int(input())
# minutes = int(input()) + 15
#
# if minutes > 59:
#     hour += 1
#     minutes -= 60
#
# if hour > 23:
#     hour -= 24
#
# if minutes < 10:
#     print(f'{hour}:0{minutes}')
# else:
#     print(f'{hour}:{minutes}')


hour = int(input())
minutes = int(input()) + 15

if minutes > 59:
    hour += 1
    minutes -= 60

if hour > 23:
    hour -= 24

if hour < 10 and minutes < 10:
    print(f'0{hour}:0{minutes}')
elif hour > 10 and minutes > 10:
    print(f'{hour}:{minutes}')
elif hour < 10 and minutes > 10:
    print(f'0{hour}:{minutes}')
elif hour > 10 and minutes < 10:
    print(f'{hour}:0{minutes}')
