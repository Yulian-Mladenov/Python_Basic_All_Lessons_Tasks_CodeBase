#user data reading
holydays = int(input())

#constant data for calculations
DAYS_IN_ONE_YEAR = 365
MINUTES_TO_PLAY_ON_HOLYDAYS = 127
MINUTES_TO_PLAY_ON_WORKING_DAYS = 63
SLEEPING_NORM = 30000
working_days_in_one_year = DAYS_IN_ONE_YEAR - holydays
holydays_hours_to_play = (holydays * MINUTES_TO_PLAY_ON_HOLYDAYS)
workingdays_hours_to_play = (working_days_in_one_year * MINUTES_TO_PLAY_ON_WORKING_DAYS)
total_time = holydays_hours_to_play + workingdays_hours_to_play

#calculations to find the difference in both times and divide them in hours and minutes
difference = abs(total_time - SLEEPING_NORM)
hours = difference // 60
minutes = difference % 60

#comapring the total time and the sleeping norm
if total_time > SLEEPING_NORM:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")





