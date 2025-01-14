# this algorithm is giving 93 points.
# entrance data
exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

# constants for the calculations
HOUR = 60
EDGE_MOMENT = 30
MINUTES = 0

# converting all the time in minutes
target_time_exam = (exam_hour * HOUR) + exam_minute
arrive_time_sum = (arrive_hour * HOUR) + arrive_minute

# that is check for ALL late conditions
if arrive_time_sum > target_time_exam:
    print("Late")
    difference = arrive_time_sum - target_time_exam
    if difference <= HOUR:
        print(f"{difference} minutes after the start")
    else:
        hours = difference // HOUR
        minutes = difference % HOUR
        if minutes < 10:
            print(f"{hours}:0{minutes} hours after the start")
        else:
            print(f"{hours}:{minutes} hours after the start")

# if is on-time punctually
elif arrive_time_sum == target_time_exam:
    print("On time")

# that is check for on-time and early not more than 30 min. condition.
elif target_time_exam - arrive_time_sum <= EDGE_MOMENT >= target_time_exam - arrive_time_sum:
    print("On time")
    difference = target_time_exam - arrive_time_sum
    print(f"{difference} minutes before the start")

# that is check for early condition
elif arrive_time_sum < target_time_exam:
    print("Early")
    difference = target_time_exam - arrive_time_sum
    if difference < HOUR:
        print(f"{difference} minutes before the start")
    else:
        hours = difference // HOUR
        minutes = difference % HOUR
        if minutes < 10:
            print(f"{hours}:0{minutes} hours before the start")
        else:
            print(f"{hours}:{minutes} hours before the start")
