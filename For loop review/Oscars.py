name_of_the_actor = input()
points_from_the_academy = float(input())
people_in_the_jury = int(input())

total_points = points_from_the_academy
TARGET_POINTS = 1250.5

for jury_member in range(people_in_the_jury):
    name_of_the_member_in_jury = len(input())
    points_from_the_member = float(input())
    total_points += (name_of_the_member_in_jury * points_from_the_member) / 2
    if total_points > TARGET_POINTS:
        print(f"Congratulations, {name_of_the_actor} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    print(f"Sorry, {name_of_the_actor} you need {TARGET_POINTS - total_points:.1f} more!")

