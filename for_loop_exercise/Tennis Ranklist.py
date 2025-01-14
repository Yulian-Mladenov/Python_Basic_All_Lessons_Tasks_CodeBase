# # user data reading
# import math
# number_of_tournament = int(input())
# initial_points = int(input())
#
# winner = 2000
# semi_final = 720
# final = 1200
#
# total_points = 0
# average_points = 0
# number_of_tournaments_won = 0
#
# # calculation of total points
# for iteration in range(number_of_tournament):
#     each_tournament = input()
#     if each_tournament == "W":
#         total_points += winner
#         number_of_tournaments_won += 1
#     elif each_tournament == "F":
#         total_points += final
#     elif each_tournament == "SF":
#         total_points += semi_final
#
# # average points calculation
# average_points = total_points / number_of_tournament
#
# # calculation how many tournaments he won
# # number_of_tournaments_won /= number_of_tournament * 100 ЗАЩО ТАКА НАПИСАНО НЕ ВРЪЩА ВЕРЕН РЕЗУЛТАТ?
# number_of_tournaments_won = (number_of_tournaments_won / number_of_tournament) * 100
#
# # results
# print(f"Final points: {total_points + initial_points}")
# print(f"Average points: {math.floor(average_points)}")
# print(f"{number_of_tournaments_won:.2f}%")

# A BIT OPTIMIZED CODE
import math
number_of_tournament = int(input())
initial_points = int(input())

total_points = 0
number_of_tournaments_won = 0

for iteration in range(number_of_tournament):
    each_tournament = input()
    if each_tournament == "W":
        total_points += 2000
        number_of_tournaments_won += 1
    elif each_tournament == "F":
        total_points += 1200
    elif each_tournament == "SF":
        total_points += 720

print(f"Final points: {total_points + initial_points}")
print(f"Average points: {math.floor(total_points / number_of_tournament)}")
print(f"{(number_of_tournaments_won / number_of_tournament) * 100:.2f}%")



