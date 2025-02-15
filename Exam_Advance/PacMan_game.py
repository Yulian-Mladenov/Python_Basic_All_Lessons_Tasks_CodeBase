# this code is 100% working correctly
def count_stars(field):
    return sum(row.count('*') for row in field)


def get_pacman_position(field):
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] == 'P':
                return i, j
    return None


def move_pacman(direction, row, col, n):
    if direction == 'up':
        row = (row - 1) % n
    elif direction == 'down':
        row = (row + 1) % n
    elif direction == 'left':
        col = (col - 1) % n
    elif direction == 'right':
        col = (col + 1) % n
    return row, col


def play_game():
    n = int(input())
    field = [list(input()) for _ in range(n)]

    health = 100
    immunity = False
    total_stars = count_stars(field)
    collected_stars = 0

    pacman_row, pacman_col = get_pacman_position(field)
    initial_position = (pacman_row, pacman_col)

    while True:
        command = input()
        if command == 'end':
            field[pacman_row][pacman_col] = 'P'
            print("Pacman failed to collect all the stars.")
            break

        if (pacman_row, pacman_col) == initial_position:
            field[pacman_row][pacman_col] = '-'

        new_row, new_col = move_pacman(command, pacman_row, pacman_col, n)

        cell = field[new_row][new_col]

        if cell == '*':
            collected_stars += 1
            field[new_row][new_col] = '-'
            if collected_stars == total_stars:
                field[new_row][new_col] = 'P'
                print("Pacman wins! All the stars are collected.")
                break

        elif cell == 'G':
            if not immunity:
                health -= 50
                if health <= 0:
                    field[new_row][new_col] = 'P'
                    print(f"Game over! Pacman last coordinates [{new_row},{new_col}]")
                    break
            immunity = False
            field[new_row][new_col] = '-'

        elif cell == 'F':
            immunity = True
            field[new_row][new_col] = '-'

        pacman_row, pacman_col = new_row, new_col

    print(f"Health: {health}")
    if collected_stars < total_stars:
        print(f"Uncollected stars: {total_stars - collected_stars}")

    for row in field:
        print(''.join(row))


play_game()
