people_in_juri = int(input())
presentations_quantity = 0
assessment_of_all_presentations = 0.0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break
    presentations_quantity += 1

    sum_of_assessment_for_each_presentation = 0.0
    for assessments in range(people_in_juri):
        assessment = float(input())
        sum_of_assessment_for_each_presentation += assessment
        assessment_of_all_presentations += assessment

    print(f"{presentation_name} - {(sum_of_assessment_for_each_presentation / people_in_juri):.2f}.")

print(f"Student's final assessment is {(assessment_of_all_presentations / presentations_quantity):.2f}.")

# how to print the average assessment of all presentations only after the name is Finish?
