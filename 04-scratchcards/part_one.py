from handle_input import read_input


def scratchcards(table):
    total_points = 0

    for row in table:
        row = row.split(':')[1].strip().split(" | ")
        winning_nums, playing_nums = row[0].split(), row[1].split()

        num_winnings = len(list(filter(lambda x: x in winning_nums, playing_nums)))

        if num_winnings > 0:
            total_points += 2 ** (num_winnings - 1)

    return total_points


print(scratchcards(read_input("input.txt")))
