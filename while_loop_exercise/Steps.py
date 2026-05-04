total_steps_quantity = 0  # total steps counter
target_steps = 10000  # target variable used to break the loop in the first condition
keyword = "Going home"  # keyword string for breaking the loop in the second condition

# logic and input data reading
while True:
    daily_steps = (input())

# first condition
    if daily_steps == keyword:
        steps_to_home = int(input())
        total_steps_quantity += steps_to_home
        if total_steps_quantity < target_steps:
            print(f"{target_steps - total_steps_quantity} more steps to reach goal.")
            break
        else:
            print("Goal reached! Good job!")
            print(f"{total_steps_quantity - target_steps} steps over the goal!")
            break

# second condition
    steps = int(daily_steps)
    total_steps_quantity += steps
    if total_steps_quantity >= target_steps:
        print("Goal reached! Good job!")
        print(f"{total_steps_quantity - target_steps} steps over the goal!")
        break


