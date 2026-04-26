# biggest_number = None
#
# while True:
#     input_number = input()
#     if input_number == "Stop":
#         print(biggest_number)
#         break
#     input_number = int(input_number)
#     if biggest_number is None or input_number > biggest_number:
#         biggest_number = input_number

input_number = input()
biggest_number = None

while input_number != 'Stop':
    if biggest_number is None or int(input_number) > biggest_number:
        biggest_number = int(input_number)
    input_number = input()

print(biggest_number)





