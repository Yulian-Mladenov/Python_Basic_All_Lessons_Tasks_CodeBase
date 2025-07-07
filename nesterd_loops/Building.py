# this is my first try without to look the lesson. Not successfull.
# floors = int(input())
# rooms_per_floor = int(input())
#
# Offices = 0
# Apartments = 0
#
# type_of_room = ''
# floor_number = 0
# room_number = 0

# with this loop you broke on indexes the floors qty, and find how much are odd and even floors have
# automatically how much apartments and offices.
# for index_of_floors in range(1, floors + 1, -1):
#     floor_number += 1
#     if index_of_floors % 2 == 0:
#         Offices += 1
#         type_of_room = 'A'
#     else:
#         Apartments += 1
#         type_of_room = 'O'
#
#     for index_of_rooms in range(rooms_per_floor + 1):
#         room_number += 1
#
#     print(f'{type_of_room}{floor_number}{room_number}')

# if len(floors) == 1:
#     type_of_room = "L"



# this code is working good, return 100 from 100 points, but is not the same as the code of the teacher.
# floors = int(input())
# rooms_per_floor = int(input())
#
# type_of_room = ''
#
# for floor_number in range(floors, 0, -1):
#     for number_of_room in range(rooms_per_floor):
#         if floor_number == floors:
#             type_of_room = "L"
#
#         elif floor_number % 2 == 0:
#             type_of_room = "O"
#
#         else:
#             type_of_room = "A"
#
#         print(f'{type_of_room}{floor_number}{number_of_room}', end=' ')
#     print()


#this is the same code has the code of the teacher, return 100 points from 100.
floors = int(input())
rooms_per_floor = int(input())

type_of_room = ''

for floor_number in range(floors, 0, -1):
    for number_of_room in range(rooms_per_floor):
        if floor_number == floors:
            type_of_room = f'"L"{floor_number}{number_of_room}'

        elif floor_number % 2 == 0:
            type_of_room = f'"O"{floor_number}{number_of_room}'

        elif floor_number % 2 != 0:
            type_of_room = f'"A"{floor_number}{number_of_room}'

        print(type_of_room, end=' ')
    print()
