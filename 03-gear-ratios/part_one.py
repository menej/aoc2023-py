from handle_input import read_input


def gear_ratios(data):
    data = [[y for y in x] for x in data]

    total = 0
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
                is_symbol = False
                k = max(i - 1, 0)
                while k < min(i + 2, len(data)) and not is_symbol:
                    if start_j - 1 >= 0:
                        char = data[k][start_j - 1]
                        if not char.isnumeric() and char != ".":
                            is_symbol = True

                    for r in range(start_j, end_j + 1):
                        char = data[k][r]
                        if not char.isnumeric() and char != ".":
                            is_symbol = True

                    if end_j + 1 < len(data[i]):
                        char = data[k][end_j + 1]
                        if not char.isnumeric() and char != ".":
                            is_symbol = True
                    k += 1
                if is_symbol:
                    total += int(num)
                num = ""
            j += 1
        i += 1
    return total


print(gear_ratios(read_input("input.txt")))
