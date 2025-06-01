starting_points = int(input())

bonus_points = 0
bonus_points_till_100 = 5
bonus_points_over_100 = starting_points * 0.20
bonus_points_over_1000 = starting_points * 0.10

if starting_points <= 100:
    bonus_points = bonus_points_till_100
elif starting_points > 1000:
    bonus_points = bonus_points_over_1000
else:
    bonus_points = bonus_points_over_100

additional_bonus_points = 0
if starting_points % 2 == 0:
    additional_bonus_points += 1
elif starting_points % 5 == 0:
    additional_bonus_points += 2

total_additional_points = additional_bonus_points + bonus_points
total_points = starting_points + total_additional_points

print(total_additional_points)
print(total_points)


