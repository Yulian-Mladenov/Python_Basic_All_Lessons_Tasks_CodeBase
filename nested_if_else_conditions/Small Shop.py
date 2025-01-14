product = input()
town = input()
quantity = float(input())

coffee_price_sofia = 0.50
coffee_price_plovdiv = 0.40
coffee_price_varna = 0.45

water_price_sofia = 0.80
water_price_plovdiv = 0.70
water_price_varna = 0.70

beer_price_sofia = 1.20
beer_price_plovdiv = 1.15
beer_price_varna = 1.10

sweets_price_sofia = 1.45
sweets_price_plovdiv = 1.30
sweets_price_varna = 1.35

peanuts_price_sofia = 1.60
peanuts_price_plovdiv = 1.50
peanuts_price_varna = 1.55

if town == "Sofia":
    if product == "coffee":
        print(coffee_price_sofia * quantity)
    elif product == "water":
        print(water_price_sofia * quantity)
    elif product == "beer":
        print(beer_price_sofia * quantity)
    elif product == "sweets":
        print(sweets_price_sofia * quantity)
    elif product == "peanuts":
        print(peanuts_price_sofia * quantity)

elif town == "Plovdiv":
    if product == "coffee":
        print(coffee_price_plovdiv * quantity)
    elif product == "water":
        print(water_price_plovdiv * quantity)
    elif product == "beer":
        print(beer_price_plovdiv * quantity)
    elif product == "sweets":
        print(sweets_price_plovdiv * quantity)
    elif product == "peanuts":
        print(peanuts_price_plovdiv * quantity)

elif town == "Varna":
    if product == "coffee":
        print(coffee_price_varna * quantity)
    elif product == "water":
        print(water_price_varna * quantity)
    elif product == "beer":
        print(beer_price_varna * quantity)
    elif product == "sweets":
        print(sweets_price_varna * quantity)
    elif product == "peanuts":
        print(peanuts_price_varna * quantity)
