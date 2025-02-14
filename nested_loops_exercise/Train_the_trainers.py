# my first try - prototype
# people_in_juri = int(input())
# score = 0
#
# while True:
#     presentation_name = input()
#
#     for iteration in range(people_in_juri):
#         grades = float(input())
#         score += grades
#         middle_grade = score / 2
#         print(f"{presentation_name} - {middle_grade:02f}.")
#
#     if presentation_name == "Finish":
#         all_presentations_average_score =
#         break

people_in_juri = int(input())
presentations_quantity = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        # probablly here schould be the average assessment of all assessments
        # average_assessment_of_all_presentation = sum_of_assessment / presentations_quantity
        break
    presentations_quantity += 1

    sum_of_assessment = 0.0
    for assessments in range(people_in_juri):
        assessment = float(input())
        sum_of_assessment += assessment

    print(f"{presentation_name} - {(sum_of_assessment / 2):.2f}.")

    print(f"Student's final assessment is {sum_of_assessment / presentations_quantity}.")


# how to print the average assessment of all presentations only after the name is Finish?
