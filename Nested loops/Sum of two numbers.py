begging_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())

counter = 0

for index_1 in range(begging_of_interval + 1):
    counter += index_1
    for index_2 in range(end_of_interval + 1):
        counter += index_2

if co
print(counter)
