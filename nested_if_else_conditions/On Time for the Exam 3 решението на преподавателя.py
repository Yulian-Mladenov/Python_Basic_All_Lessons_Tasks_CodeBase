# this code is giving 100 points
# data reading
#
# import time
# start = time.time()
#
# exam_hour = int(input())
# exam_minute = int(input())
# arrive_hour = int(input())
# arrive_minute = int(input())
#
# # constants for calculations
# HOUR = 60
# EDGE_MOMENT = 30
#
# # time calculation
# target_time_exam = (exam_hour * HOUR) + exam_minute
# arrive_time_sum = (arrive_hour * HOUR) + arrive_minute
#
# # check for exactly on time condition
# if target_time_exam == arrive_time_sum:
#     print("On time")
#     exit()
#
# # check for late condition
# if arrive_time_sum > target_time_exam:
#     print("Late")
#     difference = arrive_time_sum - target_time_exam
#     if difference < HOUR:
#         print(f"{difference} minutes after the start")
#     else:
#         hours = difference // HOUR
#         minutes = difference % HOUR
#         if minutes < 10:
#             minutes = "0" + str(minutes)
#         print(f"{hours}:{minutes} hours after the start")
#
# # check for on time in 30 minutes range and early conditions
# else:
#     difference = target_time_exam - arrive_time_sum
#     if difference <= EDGE_MOMENT:
#         print("On time")
#     else:
#         print("Early")
#     if difference < HOUR:
#         print(f"{difference} minutes before the start")
#     else:
#         hours = difference // HOUR
#         minutes = difference % HOUR
#         if minutes < 10:
#             minutes = "0" + str(minutes)
#         print(f"{hours}:{minutes} hours before the start")
#
# print(f'Time: {time.time() - start:.4f}')
# execution time: 4.4605 milliseconds


# this code is giving 100 points
# data reading

import time
start = time.time()

exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

# constants for calculations
HOUR = 60
HALF_HOUR = 30

# time calculation
target_time_exam = (exam_hour * HOUR) + exam_minute
arrive_time_sum = (arrive_hour * HOUR) + arrive_minute
difference = abs(target_time_exam - arrive_time_sum)

# check for exactly on time condition
if target_time_exam == arrive_time_sum:
    print("On time")
    exit()

# not precise filtration late,on time or early
if arrive_time_sum > target_time_exam:
    print("Late")
else:
    if difference <= HALF_HOUR:
        print("On time")
    else:
        print("Early")

# method how to check and switch before or after the target time he is arrived
after_or_before = "before"
if arrive_time_sum > target_time_exam:
    after_or_before = "after"

# this code decide he is before or after and with how much time exactly
if difference < HOUR:
    print(f"{difference} minutes {after_or_before} the start")
else:
    hours = difference // HOUR
    minutes = difference % HOUR
    if minutes < 10:
        minutes = "0" + str(minutes)
    print(f"{hours}:{minutes} hours {after_or_before} the start")

print(f'Time: {time.time() - start:.4f}')

# import time
# start = time.time()
# your code
# end
# print(f'Time: {time.time() - start}')
# execution time: 5.2658
