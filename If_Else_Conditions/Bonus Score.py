initial_points = int(input())

#това смяна само колко е бонуса
if initial_points <= 100:
    bonus_points = 5
elif initial_points < 1000:
    bonus_points = (initial_points * 0.20)
elif initial_points > 1000:
    bonus_points = (initial_points * 0.10)

#това смята колко е допълнителния бонус
if initial_points % 2 == 0:
    bonus_points = bonus_points + 1
elif initial_points % 5 == 0:
    bonus_points = bonus_points + 2

#това смята тоталния брой точки
total_points = initial_points + bonus_points

print(bonus_points)
print(total_points)
print()



