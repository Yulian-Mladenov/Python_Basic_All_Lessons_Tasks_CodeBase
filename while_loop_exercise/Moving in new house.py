# dimensions of the apartment
A = int(input())
B = int(input())
C = int(input())

#  total dimension of the flat
total_dimension_of_the_flat = A * B * C

# key values to break the loop
key_string = "Done"
total_amount_of_moved_boxes = 0

# logic
while True:
    amount_of_moved_boxes = input()  # input data
# condition one
    if amount_of_moved_boxes == key_string:
        print(f"{total_dimension_of_the_flat - total_amount_of_moved_boxes} Cubic meters left.")
        break
# condition two
    parse_data = int(amount_of_moved_boxes)
    total_amount_of_moved_boxes += parse_data
    if total_amount_of_moved_boxes > total_dimension_of_the_flat:
        print(f"No more free space! You need {total_amount_of_moved_boxes - total_dimension_of_the_flat} Cubic meters "
              f"more.")
        break
