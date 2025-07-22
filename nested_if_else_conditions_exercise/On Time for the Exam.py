# input data:
exam_time_hour = int(input())
exam_time_minutes = int(input())
arriving_time_hour = int(input())
arriving_time_minutes = int(input())

# we need to convert all hours and minutes in one complete integer number.
# That we will give us chance to calculate is later, on time or early. :
# we will convert both times - exam time and arriving time:
converting_exam_time = exam_time_hour + exam_time_minutes
converting_arriving_time = arriving_time_hour + arriving_time_minutes
if converting_exam_time > converting_arriving_time:
