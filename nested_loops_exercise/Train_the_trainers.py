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

    avg_assessment_for_each_presentation = sum_of_assessment_for_each_presentation / people_in_juri
    assessment_of_all_presentations += avg_assessment_for_each_presentation
    average_assessment_of_all_presentations = assessment_of_all_presentations / presentations_quantity

    print(f"{presentation_name} - {avg_assessment_for_each_presentation:.2f}.")

print(f"Student's final assessment is {average_assessment_of_all_presentations:.2f}.")


# how to print the average assessment of all presentations only after the name is Finish? key moments in this task:
# 1- When "break" is activated, the rest of code will be not executed, but that mean it will be not executed the code
# in the scope of the While loop only! The last print of the bottom it will be executed, because is out of the While
# loop scope. So the "break" stop execution of the code only in the while loop! 2- After each iteration in the for
# loop, the interpreter (PyCharm) do not continue to execute the code after the loop and his body! First all
# iterations are executed and store values in the variables, and then teh rst of the code (down) will be executed! 3-
# Here in this task is very clear how the position of the variables (in the different scopes) affecting the logic and
# the executed of the code, also handling the errors. Example: line 11 must be there to accumulate the assessment of
# each men of the juri, but also to e reset after new presentation came from the while loop upper. Lines 2 and 3,
# have the effect. They must be not reset after each iteration and must accumulate the values, so they must be
# positioned in the global scope of the code, out from any other scope.
