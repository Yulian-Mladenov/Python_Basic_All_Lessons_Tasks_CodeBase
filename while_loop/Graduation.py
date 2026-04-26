# name_of_the_student = input()
# passed_class_counter = 0
# non_passed_class_counter = 0
# total_annual_graduate = 0
#
# while True:
#     annual_graduate = float(input())
#     total_annual_graduate += annual_graduate
#     if annual_graduate >= 4.00:
#         passed_class_counter += 1
#         if passed_class_counter == 12:
#             print(f"{name_of_the_student} graduated. Average grade: {total_annual_graduate / 12:.2f}")
#             break
#     if annual_graduate < 4.00:
#         non_passed_class_counter += 1
#         if non_passed_class_counter > 1:
#             print(f"{name_of_the_student} has been excluded at {passed_class_counter + 1} grade")
#             break


name_of_the_student = input()
annual_graduate = float(input())
passed_class_counter = 0
non_passed_class_counter = 0
total_annual_graduate = 0

while passed_class_counter < 12 and non_passed_class_counter <= 1:
    total_annual_graduate += annual_graduate
    if annual_graduate >= 4.0:
        passed_class_counter += 1
    if passed_class_counter == 12:
        print(f"{name_of_the_student} graduated. Average grade: {total_annual_graduate / 12:.2f}")
        break

    if annual_graduate < 4.00:
        non_passed_class_counter += 1
        if non_passed_class_counter > 1:
            print(f"{name_of_the_student} has been excluded at {passed_class_counter + 1} grade")
            break
    annual_graduate = float(input())
