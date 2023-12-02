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

    total = 0

    for i, game in enumerate(games):

        minimums = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for turn in game:
            for pair in turn:
                num, color = pair.split(' ')
                num = int(num)
                if minimums[color] < num:
                    minimums[color] = num

        total += minimums['red'] * minimums['green'] * minimums['blue']

    return total


print(cube_conundrum(read_input("input.txt")))
