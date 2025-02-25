# total_tickets_quantity = 0
# finish_flag_indicator = False
#
# while True:
#     movie_name = input()
#     empty_places_for_current_movie = int(input())
#     if movie_name == "Finish":
#         finish_flag_indicator = True
#         break
#
#     ticket_quantity_per_movie = 0
#     standard_ticket = 0
#     student_ticket = 0
#     kid_ticket = 0
#
#    #while True:
#         type_of_ticket = eval(input())
#         if type_of_ticket == "End" or ticket_quantity_per_movie == empty_places_for_current_movie:
#             break
#         elif type_of_ticket == "student":
#             student_ticket += 1
#         elif type_of_ticket == "standard":
#             standard_ticket += 1
#         elif type_of_ticket == "kid":
#             kid_ticket += 1
#
#         ticket_quantity_per_movie += 1
#         total_tickets_quantity += 1
#
#     tickets_in_percentage = ((ticket_quantity_per_movie * empty_places_for_current_movie) / 100) * 100
#     print(f"{movie_name} - {tickets_in_percentage:.2f}% full.")
#
#     percentage_of_student_tickets = ((student_ticket * empty_places_for_current_movie) / 100) * 100
#     percentage_of_standard_ticket = ((standard_ticket * empty_places_for_current_movie) / 100) * 100
#     percentage_of_kid_tickets = ((kid_ticket * empty_places_for_current_movie) / 100) * 100
#
#
# if finish_flag_indicator:
#     print(f"Total tickets: {total_tickets_quantity}")
#     print(f"{percentage_of_student_tickets:.2f}% student tickets.")
#     print(f"{percentage_of_standard_ticket:.2f}% standard tickets.")
#     print(f"{percentage_of_kid_tickets:.2f}% kids tickets.")

# the result of the first movie is ok, the result of the second movie return 36,00% instead of 100.00% -  that is not
# correct. After input the keyword "Finish", instead of terminate the program and print four results, it continue to
# expect input.
# In the first test after Taxi movie the end-keyword is End,but on the second test with Scare Movie
# movie, the end-keyword is Finish! Here is the hidden problem why my program cannot print the four variables after
# keyword Finish is read and i don`t know why. Practically the key-word Finish is the next movie name

# probably solutions: the place of the code blocks and variables in the scopes are not correct. Probably is necessary
# to use flag variables to use the Finish statement to terminate the program and print the results - is not working,
# i tried.


#Claude solution one
total_tickets_quantity = 0
student_ticket_total = 0
standard_ticket_total = 0
kid_ticket_total = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break

    empty_places_for_current_movie = int(input())
    ticket_quantity_per_movie = 0

    while ticket_quantity_per_movie < empty_places_for_current_movie:
        type_of_ticket = input()
        if type_of_ticket == "End":
            break

        if type_of_ticket == "student":
            student_ticket_total += 1
        elif type_of_ticket == "standard":
            standard_ticket_total += 1
        elif type_of_ticket == "kid":
            kid_ticket_total += 1

        ticket_quantity_per_movie += 1

    # Calculate percentage for this movie
    percent_full = (ticket_quantity_per_movie / empty_places_for_current_movie) * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")

    # Add to total
    total_tickets_quantity += ticket_quantity_per_movie

# Calculate final percentages
if total_tickets_quantity > 0:  # Avoid division by zero
    percentage_of_student_tickets = (student_ticket_total / total_tickets_quantity) * 100
    percentage_of_standard_ticket = (standard_ticket_total / total_tickets_quantity) * 100
    percentage_of_kid_tickets = (kid_ticket_total / total_tickets_quantity) * 100

    print(f"Total tickets: {total_tickets_quantity}")
    print(f"{percentage_of_student_tickets:.2f}% student tickets.")
    print(f"{percentage_of_standard_ticket:.2f}% standard tickets.")
    print(f"{percentage_of_kid_tickets:.2f}% kids tickets.")
