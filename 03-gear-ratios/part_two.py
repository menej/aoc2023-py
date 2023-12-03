from handle_input import read_input
from collections import defaultdict


def gear_ratios(data):
    data = [[y for y in x] for x in data]

    counter = defaultdict(list)

    i = 0
    while i < len(data):
        num = ""
        start_j = 0
        end_j = 0

        j = 0
        while j < len(data[i]):
            char = data[i][j]
            if char.isnumeric():
                if not num:
                    start_j = end_j = j
                else:
                    end_j = j

                num += char

            if num != "" and not char.isnumeric() or num != "" and j + 1 >= len(data[i]):
                # check all adjacent

                # Run through all the valid lines (most cases three - UP, MID, BOTTOM)
                k = max(i - 1, 0)
                while k < min(i + 2, len(data)):
                    if start_j - 1 >= 0:
                        char = data[k][start_j - 1]
                        if char == "*":
                            counter[(k, start_j - 1)].append(int(num))
                            break

                    for r in range(start_j, end_j + 1):
                        char = data[k][r]
                        if char == "*":
                            counter[(k, r)].append(int(num))
                            break

                    if end_j + 1 < len(data[i]):
                        char = data[k][end_j + 1]
                        if char == "*":
                            counter[(k, end_j + 1)].append(int(num))
                            break
                    k += 1
                num = ""
            j += 1
        i += 1
    valids = [adjacent for gear, adjacent in counter.items() if len(adjacent) == 2]
    return sum([x * y for x, y in valids])


print(gear_ratios(read_input("input.txt")))
