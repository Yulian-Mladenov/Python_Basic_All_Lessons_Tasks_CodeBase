package_of_pens = 5.80
package_of_markers = 7.20
cleaning_agent_price_per_liter = 1.20

number_packages_of_pens = int(input())
number_packages_of_markers = int(input())
cleaning_agent_in_liters = int(input())
discount = int(input()) / 100

total_price_of_the_pens = number_packages_of_pens * package_of_pens
total_price_of_the_markers = number_packages_of_markers * package_of_markers
total_price_of_the_cleaning_agent = cleaning_agent_in_liters * cleaning_agent_price_per_liter

total_amount = total_price_of_the_markers + total_price_of_the_pens + total_price_of_the_cleaning_agent
total_price_after_discount = total_amount - (total_amount * discount)

print(total_price_after_discount)

