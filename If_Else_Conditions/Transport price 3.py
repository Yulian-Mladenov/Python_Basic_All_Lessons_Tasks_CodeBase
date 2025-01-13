#user data reading
kilometers = int(input())
period = input()

#constant data
taxi_first_tax = 0.70
taxi_day_tax = 0.79
taxi_night_tax = 0.90
bus_tax = 0.09
train_tax = 0.06

#math calculations
taxi_day_price = taxi_first_tax + (taxi_day_tax * kilometers)
taxi_night_price = taxi_first_tax + (taxi_night_tax * kilometers)
bus_price = bus_tax * kilometers
train_price = train_tax * kilometers

#check of the results
if kilometers < 100:
    lowest_price = bus_price
elif kilometers >= 100:
    lowest_price = train_price

if kilometers < 20 and period == "day":
    lowest_price = taxi_day_price
elif kilometers < 20 and period == "night":
    lowest_price = taxi_night_price

#print result
print(f"{lowest_price:.2f}")