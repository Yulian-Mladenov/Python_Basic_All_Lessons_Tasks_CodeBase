two_leva =
one_lev = 0
fifty_cents = 0.50
twenty_cents = 0.25
ten_cents = 0.10
five_cent = 0.05
two_cent = 0.02
one_cent = 0.01

while True:
    resto = float(input())
    parsed_sum = int(resto)
    if parsed_sum % 100 == 0:
        one_lev = 1
        print(one_lev)
        break