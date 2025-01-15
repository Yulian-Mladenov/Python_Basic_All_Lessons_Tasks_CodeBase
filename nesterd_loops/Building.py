floors = int(input())
rooms_per_floor = int(input())

even_floors = 0
O = 0

odd_floors = 0
A = 0

typ_of_room = ''
floor_number = 0
room_number = 0


# with this loop you broke on indexes the floors qty, and find how much are odd and even
# automatically how much apartments and offices.
for index_of_floors in range(floors + 1):
    floor_number += 1
    if index_of_floors % 2 == 0:
        even_floors += 1
        O += 1
    else:
        odd_floors += 1
        A += 1

    for index_of_rooms in range(rooms_per_floor + 1):
        room_number += 1

print(f'{}')





