numbers_of_the_groups = int(input())

group_Musala = 0
group_Monblan = 0
group_Kilimangaro = 0
group_K2 = 0
group_Everest = 0
total_members_from_all_groups = 0

for each_group_number in range(numbers_of_the_groups):
    members_in_each_group = int(input())
    total_members_from_all_groups += members_in_each_group
    if members_in_each_group <= 5:
        group_Musala += members_in_each_group
    elif 6 <= members_in_each_group <= 12:
        group_Monblan += members_in_each_group
    elif 13 <= members_in_each_group <= 25:
        group_Kilimangaro += members_in_each_group
    elif 26 <= members_in_each_group <= 40:
        group_K2 += members_in_each_group
    elif members_in_each_group >= 41:
        group_Everest += members_in_each_group

print(f'{(group_Musala / total_members_from_all_groups) * 100:.2f}')
print(f'{(group_Monblan / total_members_from_all_groups) * 100:.2f}')
print(f'{(group_Kilimangaro/ total_members_from_all_groups) * 100:.2f}')
print(f'{(group_K2 / total_members_from_all_groups) * 100:.2f}')
print(f'{(group_Everest / total_members_from_all_groups) * 100:.2f}')





