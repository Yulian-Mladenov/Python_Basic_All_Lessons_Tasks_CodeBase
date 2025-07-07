budget = float(input())
gpu = int(input())
cpu = int(input())
ram = int(input())

gpu_price_per_one_unit = 250
cpu_price_per_one_unit = 0.35
ram_price_per_one_unit = 0.10

total_gpu_price = gpu * gpu_price_per_one_unit

real_cpu_price_per_unit = total_gpu_price * cpu_price_per_one_unit
total_cpu_price = real_cpu_price_per_unit * cpu

real_ram_price_per_unit = total_gpu_price * ram_price_per_one_unit
total_ram_price = real_ram_price_per_unit * ram

total_price_for_all = total_ram_price + total_cpu_price + total_gpu_price

if gpu > cpu:
    total_price_for_all -= total_price_for_all * 0.15
else:
    total_price_for_all = total_price_for_all

difference = abs(budget - total_price_for_all)

if total_price_for_all <= budget:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
