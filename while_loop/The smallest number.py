biggest_number = None

while True:
    input_number = input()
    if input_number == "Stop":
        print(biggest_number)
        break
    input_number = int(input_number)
    if biggest_number is None or input_number < biggest_number:
        biggest_number = input_number