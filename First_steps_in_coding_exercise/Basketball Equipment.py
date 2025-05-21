anual_tax_for_training = int(input())

bascketball_sneackers_price_in_percentage = 0.40
basketball_suit_price_in_percentage = 0.20
bascketball_ball_price_in_percentage = 0.25
bascketball_accessories_price_in_percentage = 1 / 5

bascketball_sneakers_price = anual_tax_for_training - (
            anual_tax_for_training * bascketball_sneackers_price_in_percentage)
bascketball_suit_price = bascketball_sneakers_price - (bascketball_sneakers_price * basketball_suit_price_in_percentage)
basketball_ball_price = bascketball_suit_price - (bascketball_suit_price * bascketball_ball_price_in_percentage)
bascketball_acesories_price = basketball_ball_price - (basketball_ball_price * 0.20)

total_cost_for_all = bascketball_acesories_price + bascketball_suit_price + bascketball_sneakers_price + basketball_ball_price

print(total_cost_for_all)
