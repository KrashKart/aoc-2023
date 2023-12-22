FNAME = "day_22.txt"
bricks = []

with open(FNAME, "r") as f:
    for line in f:
        a, b = line.strip().split("~")
        a, b = tuple(map(int, a.split(","))), tuple(map(int, b.split(",")))
        bricks.append(a + b)

bricks = sorted(bricks, key=lambda x: x[2])

def fall(heights, b):
    max_height = 0
    for i in range(b[0], b[3] + 1):
        for j in range(b[1], b[4] + 1):
            max_height = max(max_height, heights.get((i, j), 0))
    dist = max(b[2] - max_height - 1, 0)
    return (b[0], b[1], b[2] - dist, b[3], b[4], b[5] - dist)

def drop(bricks):
    heights = dict()
    fallen = []
    falls = 0
    for brick in bricks:
        fell = fall(heights, brick)
        if fell[2] != brick[2]:
            falls += 1
        fallen.append(fell)
        for x in range(brick[0], brick[3] + 1):
            for y in range(brick[1], brick[4] + 1):
                heights[(x, y)] = fell[5]
    return falls, fallen

def part_1():
    _, fallen = drop(bricks)
    tot = 0
    for i in range(len(fallen)):
        without = fallen[:i] + fallen[i + 1:]
        falls, _ = drop(without)
        if not falls:
            tot += 1
    print(tot)

def part_2():
    _, fallen = drop(bricks)
    tot = 0
    for i in range(len(fallen)):
        without = fallen[:i] + fallen[i + 1:]
        falls, _ = drop(without)
        tot += falls
    print(tot)

part_1()
part_2()