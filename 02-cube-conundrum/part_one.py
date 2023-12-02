import re

from handle_input import read_input

valids = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def cube_conundrum(data):
    games = []
    for line in data:
        games.append([x.strip().split(', ') for x in line.split(":")[1].split(";")])

    num_valids = 0
    for i, game in enumerate(games):
        is_valid = True

        for turn in game:
            for pair in turn:
                num, color = pair.split(' ')
                if int(num) > valids[color]:
                    is_valid = False
                    break

            if not is_valid:
                break

        if is_valid:
            num_valids += i + 1

    return num_valids


print(cube_conundrum(read_input("input.txt")))
