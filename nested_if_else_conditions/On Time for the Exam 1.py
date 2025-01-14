#entrance data
exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

#constants for the calculations
HOUR = 60
CONSTANT_MINUTES = 10

#converting all the time in minutes
target_time_exam = (exam_hour * HOUR) + exam_minute
arrive_time_sum = (arrive_hour * HOUR) + arrive_minute
difference = abs(target_time_exam - arrive_time_sum)

target_on_time = 30
result_answer = ""
#that is check for late condition
if arrive_time_sum > target_time_exam:
    result_answer = "Late"

#that is check for on-time condition.On the second line is the case that is early or later according the exam time target.
elif difference <= target_on_time or target_time_exam == arrive_time_sum:
    if difference + arrive_time_sum <= target_time_exam:
        result_answer = "On time"

#that is check for early condition
elif difference > target_on_time:
    result_answer = "Early"

print(result_answer)

hours = 0
minutes = 0

if arrive_time_sum != target_on_time:
    if difference >= HOUR and arrive_time_sum < target_on_time:
        if difference >= HOUR:
            hours += 1
            minutes = difference - HOUR
            print(f"{hours}:{minutes} hours before the start")
        else:
            minutes = difference
            print(f"{minutes} minutes before the start")

    elif difference >= HOUR and arrive_time_sum > target_on_time:
        if difference >= HOUR:
            hours += 1
            minutes = difference - HOUR
            print(f"{hours}:{minutes} hours after the start")
        else:
            minutes = difference
            print(f"{minutes} minutes after the start")



# if minutes_1 >= 60:
#     hours_1 = hours_1 + 1
#     minutes_1 = minutes_1 - 60
#
# if hours_1 > 23:
#      hours_1 = hours_1 - 24
#
# if minutes_1 < 10:
#     print(f'{hours_1}:0{minutes_1}')
# else:
#     print(f'{hours_1}:{minutes_1}')








