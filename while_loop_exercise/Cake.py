# input data of the cake
dimension_A = int(input())
dimension_B = int(input())

# how much pieces have the cake
cake_quantity = dimension_A * dimension_B

# key values to break the loop
key_string = "STOP"
total_amount_of_taken_pieces = 0

# logic
while True:
    amount_of_taken_pieces = input()  # input data
# condition one
    if amount_of_taken_pieces == key_string:
        print(f"{cake_quantity - total_amount_of_taken_pieces} pieces are left.")
        break
# condition two
    parse_data = int(amount_of_taken_pieces)
    total_amount_of_taken_pieces += parse_data
    if total_amount_of_taken_pieces > cake_quantity:
        print(f"No more cake left! You need {total_amount_of_taken_pieces - cake_quantity} pieces more.")
        break

