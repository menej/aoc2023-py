def seed_fertilizer():
    seeds, *blocks = open("input.txt").read().split('\n\n')

    seeds = list(map(int, seeds.split(":")[1].split()))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            a, b, c = map(int, line.split())
            ranges.append((a, b, c))

        new = []

        for x in seeds:
            for a, b, c in ranges:
                if x in range(b, b + c):
                    new.append(x - b + a)
                    break
            else:
                new.append(x)
        seeds = new

    return min(seeds)

print(seed_fertilizer())

