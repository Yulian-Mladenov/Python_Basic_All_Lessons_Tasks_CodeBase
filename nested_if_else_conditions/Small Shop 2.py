product = input()
town = input()
quantity = float(input())

price = 0

if town == "Sofia":
    if product == "coffee":
        price = 0.50
    elif product == "water":
        price = 0.80
    elif product == "beer":
        price = 1.20
    elif product == "sweets":
        price = 1.45
    elif product == "peanuts":
        price = 1.60
    else:
        print("unknown")
elif town == "Plovdiv":
    if product == "coffee":
        price = 0.40
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.15
    elif product == "sweets":
        price = 1.30
    elif product == "peanuts":
        price = 1.50
    else:
        print("unknown")
elif town == "Varna":
    if product == "coffee":
        price = 0.45
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.10
    elif product == "sweets":
        price = 1.35
    elif product == "peanuts":
        price = 1.55
    else:
        print("unknown")
else:
    print("unknown")


if price == 0:
    print("unknown")
else:
    price *= quantity
    print(price)




























