# dimensions in centimeters
length = int(input())
width = int(input())
high = int(input())
occupied_percentage_of_the_aquarium = float(input()) / 100

total_volume_of_empty_aquarium = length * width * high * 0.001

volume_with_accessories = total_volume_of_empty_aquarium - (total_volume_of_empty_aquarium * occupied_percentage_of_the_aquarium)

print(volume_with_accessories)
