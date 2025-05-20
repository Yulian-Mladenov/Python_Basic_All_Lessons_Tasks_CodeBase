name_of_the_architect = input()
number_of_projects_for_each_architect = int(input())

necessary_time_to_create_one_project = 3

total_time = number_of_projects_for_each_architect * necessary_time_to_create_one_project

print(f"The architect {name_of_the_architect} will need {total_time} hours to complete {number_of_projects_for_each_architect} project/s.")