#reading user data
number_magnolia = int(input())
number_zymbyl = int(input())
number_roses = int(input())
number_cactus = int(input())
gift_price = float(input())

#Constant Initialization
magnolia = 3.25
zymbyl = 4
rose = 3.50
cactus = 8

#math calculations
total_brutto_sum = (number_magnolia * magnolia) + (number_zymbyl * zymbyl) +\
                   (number_roses * rose) + (number_cactus * cactus)

total_netto_sum = total_brutto_sum - (total_brutto_sum * 0.05)

import math
difference = math.floor(abs(total_netto_sum - gift_price))
difference_2 = math.ceil(abs(total_netto_sum - gift_price))

#final if-else statement check
if total_netto_sum >= gift_price:
    print(f"She is left with {difference} leva.")
else:
    print(f"She will have to borrow {difference_2} leva.")





