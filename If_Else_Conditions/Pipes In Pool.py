#reading data from user
volume = int(input())
debit_p1 = int(input())
debit_p2 = int(input())
time = float(input())

#find volumes of each pipe and total from both of them
volume_p1 = debit_p1 * time
volume_p2 = debit_p2 * time
total_volume = volume_p1 + volume_p2

#find the quatity in percents
v_p1_in_percents = (volume_p1 / total_volume) * 100
v_p2_in_percents = (volume_p2 / total_volume) * 100
total_volume_percentage = (total_volume / volume) * 100

#variable to find the difference between both volumes
if_pool_is_overfull = abs(volume - total_volume)

#check of the situation after N hours
if total_volume <= volume:
    print(f"The pool is {total_volume_percentage:.2f}% full. Pipe 1: {v_p1_in_percents:.2f}%. Pipe 2: {v_p2_in_percents:.2f}%.")
else:
    print(f"For {time} hours the pool overflows with {if_pool_is_overfull:.2f} liters.")

