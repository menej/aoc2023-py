import math
import re

from handle_input import read_input


def wait_for_it(data):
    times = re.split(r'\s+', data[0].split(":")[1].strip())
    distances = re.split(r'\s+', data[1].split(":")[1].strip())
    pairs = [(int(x), int(y)) for x, y in zip(times, distances)]

    total = 1
    for time, distance in pairs:
        n = 0
        for speed in range(0, math.ceil(time / 2) if time % 2 == 1 else time // 2 + 1):
            time_left = time - speed
            total_dist = speed * time_left

            if total_dist > distance:
                n += 1

        if time % 2 == 0:
            n = n * 2 - 1
        else:
            n = n * 2

        total *= n

    return total


print(wait_for_it(read_input("input.txt")))
