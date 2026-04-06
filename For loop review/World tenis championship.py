import math
number_of_tournament = int(input())
initial_points = int(input())

# various classifications
W = 2000  # winner
F = 1200  # finalist
SF = 720  # semi finalist
total_points = initial_points
how_many_wins = 0

for tournament in range(number_of_tournament):
    classification = input()
    if classification == 'W':
        total_points += W
        how_many_wins += 1
    elif classification == 'F':
        total_points += F
    elif classification == 'SF':
        total_points += SF

average_points = math.floor((total_points - initial_points) / number_of_tournament)
tournaments_won = (how_many_wins / number_of_tournament) * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{tournaments_won:.2f}%")

