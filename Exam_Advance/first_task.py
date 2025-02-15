# from collections import deque
#
#
# def alchemy_lab(substances, crystals):
#     potions = {
#         110: "Brew of Immortality",
#         100: "Essence of Resilience",
#         90: "Draught of Wisdom",
#         80: "Potion of Agility",
#         70: "Elixir of Strength"
#     }
#
#     crafted_potions = set()
#     crafted_order = []
#
#     substances = list(map(int, substances.split(", ")))  # Stack (LIFO)
#     crystals = deque(map(int, crystals.split(", ")))  # Queue (FIFO)
#
#     while substances and crystals and len(crafted_potions) < 5:
#         substance = substances.pop()
#         crystal = crystals.popleft()
#         total_energy = substance + crystal
#
#         # Check if exact potion exists and is not yet crafted
#         if total_energy in potions and potions[total_energy] not in crafted_potions:
#             crafted_potions.add(potions[total_energy])
#             crafted_order.append(potions[total_energy])
#         else:
#             # Find the highest potion that can be crafted
#             possible_potions = [e for e in potions if e <= total_energy and potions[e] not in crafted_potions]
#             if possible_potions:
#                 best_match = max(possible_potions)  # Highest potion
#                 crafted_potions.add(potions[best_match])
#                 crafted_order.append(potions[best_match])
#                 remaining_energy = total_energy - best_match
#                 if remaining_energy > 0:
#                     crystals.append(remaining_energy)  # Reduce energy by 20
#             else:
#                 # If no potion can be crafted
#                 crystal -= 5
#                 if crystal > 0:
#                     crystals.append(crystal)  # Reduce by 5 and add back
#
#     if len(crafted_potions) == 5:
#         print("Success! The alchemist has forged all potions!")
#     else:
#         print("The alchemist failed to complete his quest.")
#
#     if crafted_order:
#         print("Crafted potions:", ", ".join(crafted_order))
#
#     if substances:
#         print("Substances:", ", ".join(map(str, reversed(substances))))
#
#     if crystals:
#         print("Crystals:", ", ".join(map(str, crystals)))
#
#
# substances_input = "45, 65, 35, 25, 70"
# crystals_input = "15, 30, 20, 10, 5, 40"
#
# alchemy_lab(substances_input, crystals_input)


# from collections import deque
#
#
# def craft_potions(substances, crystals):
#     substances_stack = [int(x.strip()) for x in substances.split(", ")]
#     crystals_queue = deque([int(x.strip()) for x in crystals.split(", ")])
#
#     potions = {
#         "Brew of Immortality": 110,
#         "Essence of Resilience": 100,
#         "Draught of Wisdom": 90,
#         "Potion of Agility": 80,
#         "Elixir of Strength": 70
#     }
#
#     crafted_potions = []
#
#     while substances_stack and crystals_queue and len(crafted_potions) < 5:
#         current_substance = substances_stack.pop()
#         current_crystal = crystals_queue.popleft()
#         combined_energy = current_substance + current_crystal
#
#         potion_crafted = False
#
#         for potion_name, energy_required in potions.items():
#             if energy_required == combined_energy and potion_name not in crafted_potions:
#                 crafted_potions.append(potion_name)
#                 potion_crafted = True
#                 break
#
#         if not potion_crafted:
#             possible_potions = {name: energy for name, energy in potions.items()
#                                 if energy < combined_energy and name not in crafted_potions}
#
#             if possible_potions:
#                 best_potion = max(possible_potions.items(), key=lambda x: x[1])
#                 crafted_potions.append(best_potion[0])
#                 reduced_crystal = current_crystal - 20
#                 if reduced_crystal > 0:
#                     crystals_queue.append(reduced_crystal)
#             else:
#                 reduced_crystal = current_crystal - 5
#                 if reduced_crystal > 0:
#                     crystals_queue.append(reduced_crystal)
#
#     success = len(crafted_potions) == 5
#     result = []
#
#     if success:
#         result.append("Success! The alchemist has forged all potions!")
#     else:
#         result.append("The alchemist failed to complete his quest.")
#
#     if crafted_potions:
#         result.append(f"Crafted potions: {', '.join(crafted_potions)}")
#
#     if substances_stack:
#         result.append(f"Substances: {', '.join(map(str, reversed(substances_stack)))}")
#
#     if crystals_queue:
#         result.append(f"Crystals: {', '.join(map(str, crystals_queue))}")
#
#     return result
#
#
# def run_test_case(substances, crystals):
#     print("\nInput:")
#     print(substances)
#     print(crystals)
#     print("\nOutput:")
#     result = craft_potions(substances, crystals)
#     for line in result:
#         print(line)
#
#
# # Test case 1
# test_substances1 = "40, 5, 80, 60, 75, 60, 65, 70"
# test_crystals1 = "20, 35, 45, 25, 10, 30, 15"
# run_test_case(test_substances1, test_crystals1)
#
# # Test case 2
# test_substances2 = "45, 65, 35, 25, 70"
# test_crystals2 = "15, 30, 20, 10, 5, 40"
# run_test_case(test_substances2, test_crystals2)


# this code is working on 100%
from collections import deque


def solve(substances, crystals):
    substances_stack = [int(x.strip()) for x in substances.split(", ")]
    crystals_queue = deque([int(x.strip()) for x in crystals.split(", ")])

    potions = {
        "Brew of Immortality": 110,
        "Essence of Resilience": 100,
        "Draught of Wisdom": 90,
        "Potion of Agility": 80,
        "Elixir of Strength": 70
    }

    crafted_potions = []

    while substances_stack and crystals_queue and len(crafted_potions) < 5:
        current_substance = substances_stack.pop()
        current_crystal = crystals_queue.popleft()
        combined_energy = current_substance + current_crystal

        potion_crafted = False

        for potion_name, energy_required in potions.items():
            if energy_required == combined_energy and potion_name not in crafted_potions:
                crafted_potions.append(potion_name)
                potion_crafted = True
                break

        if not potion_crafted:
            possible_potions = {name: energy for name, energy in potions.items()
                                if energy < combined_energy and name not in crafted_potions}

            if possible_potions:
                best_potion = max(possible_potions.items(), key=lambda x: x[1])
                crafted_potions.append(best_potion[0])
                reduced_crystal = current_crystal - 20
                if reduced_crystal > 0:
                    crystals_queue.append(reduced_crystal)
            else:
                reduced_crystal = current_crystal - 5
                if reduced_crystal > 0:
                    crystals_queue.append(reduced_crystal)

    if len(crafted_potions) == 5:
        print("Success! The alchemist has forged all potions!")
    else:
        print("The alchemist failed to complete his quest.")

    if crafted_potions:
        print(f"Crafted potions: {', '.join(crafted_potions)}")

    if substances_stack:
        substances_str = ', '.join(str(x) for x in reversed(substances_stack))
        print(f"Substances: {substances_str}")

    if crystals_queue:
        crystals_str = ', '.join(str(x) for x in crystals_queue)
        print(f"Crystals: {crystals_str}")


substances = input()
crystals = input()
solve(substances, crystals)
