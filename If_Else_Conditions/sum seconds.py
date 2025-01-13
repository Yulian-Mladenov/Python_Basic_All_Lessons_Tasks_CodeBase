# Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50).
# Да се напише програма, която чете времената на състезателите в секунди,
# въведени от потребителя и пресмята сумарното им време във формат "минути:секунди".
# Секундите да се изведат с водеща нула (2 à "02", 7 à "07", 35 à "35").

person_1 = int(input())
person_2 = int(input())
person_3 = int(input())

total_time = person_3 + person_2 + person_1

import math
minutes = math.floor(total_time // 60)
seconds = total_time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f'{minutes}:{seconds}')



#print(f"{minutes}:{round(seconds, 2)}")

#print(f"{minutes}:{seconds:.2f}")


# if total_time <= 60:
#     minutes = total_time
#     seconds = total_time - 60
#     print(f"{minutes}:{seconds}")
# elif total_time > 60:
#     minutes = total_time
#     seconds = total_time - 60
#     print(f"{minutes}:{seconds}")




