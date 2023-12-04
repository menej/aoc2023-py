import re

from handle_input import read_input


def scratchcards(table):
    total_cards = 0

    cache = {}

    clean_table = []
    for row in table:
        game, row = row.split(':')

        game = re.search(r"\d+", game).group()

        row = row.strip().split(" | ")
        winning_nums, playing_nums = row[0].split(), row[1].split()

        cache[game] = (winning_nums, playing_nums)
        clean_table.append(game)

    while clean_table:
        game = clean_table.pop()
        total_cards += 1

        winning_nums, playing_nums = cache[game]

        num_winnings = len(list(filter(lambda x: x in winning_nums, playing_nums)))

        for _ in range(num_winnings):
            game = int(game) + 1
            clean_table.append(str(game))
    return total_cards


print(scratchcards(read_input("input.txt")))
