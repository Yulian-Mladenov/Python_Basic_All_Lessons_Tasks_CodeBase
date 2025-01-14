import time
start = time.process_time()

days_to_stay = int(input())
type_of_accommodation = input()
rating = input()

# prices
room_for_one_person = 18
apartment = 25
president_apartment = 35

#constant for the calculations
real_nights_count = 1

# rating discounts
percent_positive_rating = 25 / 100
percent_negative_rating = 10 / 100

# apartment discounts
less_than_10_days_1 = 30 / 100
between_10_15_days_1 = 35 / 100
more_than_15_days_1 = 50 / 100

#discount for president apartment
less_than_10_days_2 = 10 / 100
between_10_15_days_2 = 15 / 100
more_than_15_days_2 = 20 / 100

# days constants for calculations
les_than_10_days = 10
between_10_15_days_low = 10
between_10_15_days_hi = 15
more_than_15_days = 15

# колко филтрирания имаш на брой?
# и колко на брой данни имаш да филтрираш?
# какво се търси в задачата?Крайната цена.
# как се намира тя?
# напиши код който намира общия брой нощувки за целия престой.За да стане това,ти трябват нощувките и цената.Първото е константа,второто се филтрира и използва за смятане.Сшед като този етап е готов,преминаваш към намиране на отстъпката.
# Как се намира отстъпка на цена?
# по какъв начин,с какъв код ще.направиш всичко това дотук?
# след като филтрираш цената втори път,трябва да пресметнеш дали е дал оценка и каква е,и на база това,да промениш цената още веднъж.

price = days_to_stay * type_of_accommodation

# тук има избор,тъй като дните са в една променлива и тя не е необходимо да се променя ,за да се оптимизиря кода,то я пишем само и това е.Но променливата за дните,може да бъде променяна директно или може да се мени чрез друга променлива,помнейки я в нея.

if type_of_accommodation == "room for one person":
    price = (days_to_stay - real_nights_count) * room_for_one_person

# свга можеш да продължиш със елиф надолу,защото това условие за настанявсне за сам човек е покрито напълно.

elif type_of_accommodation == "apartment":
    price = (days_to_stay - real_nights_count) * apartment
    if days_to_stay - real_nights_count < les_than_10_days:
        price -= price * less_than_10_days_1
    elif les_than_10_days < days_to_stay - real_nights_count < between_10_15_days_hi:
        price -= price * between_10_15_days_1
    elif days_to_stay - real_nights_count > more_than_15_days:
        price -= price * more_than_15_days_1

elif type_of_accommodation == "president apartment":
    price = (days_to_stay - real_nights_count) * president_apartment
    if days_to_stay - real_nights_count < les_than_10_days:
        price -= price * less_than_10_days_2
    elif les_than_10_days < days_to_stay - real_nights_count < between_10_15_days_hi:
        price -= price * between_10_15_days_2
    elif days_to_stay - real_nights_count > more_than_15_days:
        price -= price * more_than_15_days_2

if rating == "positive":
    price += price * percent_positive_rating
else:
    price -= price * percent_negative_rating

print(f"{price:.2f}")

print(time.process_time() - start)
# тук си филтрирал най-лесното условие.Сега трябва да го филтрираш втори път.
# за второто филтриране,ще е необходимо да изчислиш процент от цената.Какви варианти знаеш?