# reading data from user
# how_much_groups = int(input())
#
# Musala_people = 0
# Mont_Blanc_people = 0
# Kilimanjaro_people = 0
# K2_people = 0
# Everest_people = 0
#
# total_number_people = 0
#
# for iteration in range(how_much_groups):
#     how_many_people_in_each_group = int(input())
#     if how_many_people_in_each_group <= 5:
#         Musala_people += how_many_people_in_each_group
#         total_number_people += Musala_people
#     elif 6 <= how_many_people_in_each_group <= 12:
#         Mont_Blanc_people += how_many_people_in_each_group
#         total_number_people += Mont_Blanc_people
#     elif 13 <= how_many_people_in_each_group <= 25:
#         Kilimanjaro_people += how_many_people_in_each_group
#         total_number_people += Kilimanjaro_people
#     elif 26 <= how_many_people_in_each_group <= 40:
#         K2_people += how_many_people_in_each_group
#         total_number_people += K2_people
#     elif how_many_people_in_each_group >= 41:
#         Everest_people += how_many_people_in_each_group
#         total_number_people += Everest_people
#
# print(f"{(Musala_people / total_number_people) * 100:.2f}%")
# print(f"{(Mont_Blanc_people / total_number_people) * 100:.2f}%")
# print(f"{(Kilimanjaro_people / total_number_people) * 100:.2f}%")
# print(f"{(K2_people / total_number_people) * 100:.2f}%")
# print(f"{(Everest_people / total_number_people) * 100:.2f}%")

#  total_number_people += Musala_people
# този код няма да връща верни резултати,защото по този начин общия брой на хората не се натрупва,
# вместо това се занулява всеки път и се дава новата стойност която се получава след провреката.
# За да работи нормално кода,трябва броя на хората да се натрупва след всяка итерация веднага след нея,но без да влиза надолу в проверките.
# На 15-ти ред се вижда че към Musala_people след всяка итерация към нейната стойност се добавя количеството на хора за текущата итерация.
# Тоест след всяка итерация стойността на тази променлива се променя с нова.Демек занулява се и се дава нова стойност,тоест без натпрупване.
# Което е добре,така трябва да бъде. При 16-ти ред се случва същото нещо, всеки път на променливата   total_number_people се дава нова стойност.
# На 19-ти , 22-ри, 25-ти и 28-ми редове е същото нещо. Това във ефект прави така, че след всяка итерация стойността на  total_number_people се занулява и се дава нова.
# Но това не ни върши работа, защото целта на  total_number_people е да увеличава стойността си след всяка итерация, а не да се занулява и да и се присвоява нова.
# По този начин със натрупване на стойонстта се получава общия брой на хората, а със зануляване всеки път се получава броя на хората само след всяка итерация.
# Затова  total_number_people трябва да бъде горе след цикъла,за да може просто да добавя нови и нови стойности с натрупване без да трие старите стойности.
# В долния код се вижда,че  total_number_people фигурира само веднъж след цикъла и така натрупва броя на хората след всеки цикъл.

how_much_groups = int(input())

Musala_people = 0
Mont_Blanc_people = 0
Kilimanjaro_people = 0
K2_people = 0
Everest_people = 0

total_number_people = 0

for iteration in range(how_much_groups):
    how_many_people_in_each_group = int(input())
    total_number_people += how_many_people_in_each_group
    if how_many_people_in_each_group <= 5:
        Musala_people += how_many_people_in_each_group
    elif 6 <= how_many_people_in_each_group <= 12:
        Mont_Blanc_people += how_many_people_in_each_group
    elif 13 <= how_many_people_in_each_group <= 25:
        Kilimanjaro_people += how_many_people_in_each_group
    elif 26 <= how_many_people_in_each_group <= 40:
        K2_people += how_many_people_in_each_group
    elif how_many_people_in_each_group >= 41:
        Everest_people += how_many_people_in_each_group

print(f"{(Musala_people / total_number_people) * 100:.2f}%")
print(f"{(Mont_Blanc_people / total_number_people) * 100:.2f}%")
print(f"{(Kilimanjaro_people / total_number_people) * 100:.2f}%")
print(f"{(K2_people / total_number_people) * 100:.2f}%")
print(f"{(Everest_people / total_number_people) * 100:.2f}%")




