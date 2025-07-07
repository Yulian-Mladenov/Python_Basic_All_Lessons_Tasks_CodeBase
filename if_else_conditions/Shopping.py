#data from user
budget = float(input())
gpu = int(input())
cpu = int(input())
ram = int(input())

#calculating prices by each piece
GPU_PRICE = 250
total_gpu_price = gpu * GPU_PRICE
one_cpu_price = total_gpu_price * 0.35
one_ram_price = total_gpu_price * 0.10
total_price_cpus = cpu * one_cpu_price
total_price_rams = ram * one_ram_price

#total price calculating
total_price = total_gpu_price + total_price_rams + total_price_cpus

#discount calculating
discount = total_price * 0.15

#new variables and if-else block to switch the prices.This is the first check.
total_price_1 = total_price - discount
total_price_2 = total_price
if gpu > cpu:
    total_price = total_price_1
else:
    total_price = total_price_2

#variable to find the differences betwenn budget and final price,choose from the upper if-else block
difference = abs(total_price - budget)

#final if-else block to check the both sums and print the difference.This is the second chek.
if total_price_1 < budget:
    print(f"You have {difference:.2f} leva left!")
elif total_price_1 > budget:
    print(f"Not enough money! You need {difference:.2f} leva more!")
elif total_price_2 < budget:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")


















