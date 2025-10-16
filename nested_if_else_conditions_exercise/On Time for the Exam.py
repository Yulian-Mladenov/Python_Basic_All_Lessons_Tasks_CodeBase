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

# if he came early with less than one hour:
if arriving_time_minutes >= exam_time_minutes:
    difference = arriving_time_minutes - exam_time_minutes
    if difference <= 59:
        if difference < 10:
            print(f'0{difference} minutes before the start')
        else:
            print(f'{difference:.2f} minutes before the start')

# if he came early with more than one hour:
elif

