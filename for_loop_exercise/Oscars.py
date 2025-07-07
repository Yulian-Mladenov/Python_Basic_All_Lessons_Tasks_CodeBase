actor_name = input()
points_given_by_the_academy = float(input())
number_of_evaluators = int(input())

nomination_target = 1250.5
enough_points = False

for iteration in range(number_of_evaluators):
    each_evaluator = input()
    given_points = float(input())
    points_given_by_the_academy += ((len(each_evaluator) * given_points) / 2)

    if points_given_by_the_academy >= nomination_target:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points_given_by_the_academy:.1f}!")
        enough_points = True
        break

if not enough_points:
    print(f"Sorry, {actor_name} you need {nomination_target - points_given_by_the_academy:.1f} more!")