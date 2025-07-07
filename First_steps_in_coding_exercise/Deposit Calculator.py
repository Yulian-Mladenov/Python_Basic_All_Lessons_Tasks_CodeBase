amount_deposited = float(input())
deposit_term = int(input())
annual_interest_rate = float(input()) / 100

interest = amount_deposited * annual_interest_rate

interest_per_month = interest / 12

total_amount = amount_deposited + (deposit_term * interest_per_month)

print(total_amount)
