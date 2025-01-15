floors = int(input())
rooms_per_floor = int(input())

Offices = 0
Apartments = 0

type_of_room = ''
floor_number = 0
room_number = 0


# with this loop you broke on indexes the floors qty, and find how much are odd and even floors have
# automatically how much apartments and offices.
for index_of_floors in range(1, floors + 1, -1):
    floor_number += 1
    if index_of_floors % 2 == 0:
        Offices += 1
        type_of_room = 'A'
    else:
        Apartments += 1
        type_of_room = 'O'

    for index_of_rooms in range(rooms_per_floor + 1):
        room_number += 1

    print(f'{type_of_room}{floor_number}{room_number}')



# if len(floors) == 1:
#     type_of_room = "L"


