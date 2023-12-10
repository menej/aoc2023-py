from handle_input import read_input

def haunted_wasteland(data):
    seq = data.pop(0)
    data.pop(0)

    mappings = {}
    for d in data:
        place, coords = d.split(" = ")
        coords = tuple(coords.lstrip("(").rstrip(")").split(", "))
        mappings[place] = coords

    current = "AAA"

    i = 0
    max_i = len(seq) - 1
    steps = 0
    while current != "ZZZ":
        next_move = seq[i]

        if next_move == "L":
            current = mappings[current][0]
        else:
            current = mappings[current][1]

        steps += 1

        if i >= max_i:
            i = 0
        else:
            i += 1

    return steps


print(haunted_wasteland(read_input("input.txt")))