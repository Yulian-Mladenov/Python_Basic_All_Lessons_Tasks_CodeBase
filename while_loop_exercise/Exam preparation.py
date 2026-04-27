poor_rating = int(input())
number_of_all_tasks = 0
total_rating = 0
number_of_poor_rating = 0
last_task = ''

while True:
    task_name = input()
    if task_name == "Enough":
        print(f"Average score: {total_rating / number_of_all_tasks:.2f}")
        print(f"Number of problems: {number_of_all_tasks}")
        print(f"Last problem: {last_task}")
        break
    last_task = task_name
    rating = int(input())
    total_rating += rating
    number_of_all_tasks += 1
    if rating <= 4:
        number_of_poor_rating += 1
        if number_of_poor_rating >= poor_rating:
            print(f"You need a break, {number_of_poor_rating} poor grades.")
            break
