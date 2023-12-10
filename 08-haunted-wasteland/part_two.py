from math import gcd

# NOTE: solved with help

steps, _, *rest = open("input.txt").read().splitlines()

network = {}

for line  in rest:
    pos, targets = line.split(" = ")
    network[pos] = targets[1:-1].split(", ")

positions = [key for key in network if key.endswith("A")]
cycles = []

for current in positions:
    cycle = []

    current_steps = steps
    step_count = 0
    first_z = None

    while True:
        while step_count == 0 or not current.endswith("Z"):
            step_count += 1
            current = network[current][0 if current_steps[0] == "L" else 1]
            current_steps = current_steps[1:] + current_steps[0]

        cycle.append(step_count)

        # We have arrived at the first Z
        if first_z is None:
            first_z = current
            step_count = 0
        # We have back at the first Z in a new cycle
        elif current == first_z:
            break
        # We have arrived at different Z
    cycles.append(cycle)

nums = [cycle[0] for cycle in cycles]

lcm = nums.pop()

for num in nums:
    lcm = lcm * num // gcd(lcm, num)

print(lcm)