budget = float(input())
season = input()

destination = ''
price = 0
accommodation_type = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = budget * 0.30
        accommodation_type = 'Camp'
    elif season == 'winter':
        price = budget * 0.70
        accommodation_type = 'Hotel'

elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = budget * 0.40
        accommodation_type = 'Camp'
    elif season == 'winter':
        price = budget * 0.80
        accommodation_type = 'Hotel'

elif budget > 1000:
    destination = 'Europe'
    price = budget * 0.90
    accommodation_type = 'Hotel'

spend_money = abs(budget - price)

print(f"Somewhere in {destination}")
print(f"{accommodation_type} - {price:.2f}")








