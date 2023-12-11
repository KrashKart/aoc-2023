from itertools import combinations

FNAME = "day_11.txt"
def expand(fname, factor):
    factor -= 1
    img = []
    gals = []
    rows_empty = []
    cols_empty = []
    with open(fname, "r") as f:
        for idx, line in enumerate(f):
            if "#" not in line:
                rows_empty.append(idx)
            img.append(list(line.strip()))
    
    for cols in range(len(img[0])):
        if not list(filter(lambda x: x[cols] == "#", img)):
            cols_empty.append(cols)

    for r in range(len(img)):
        for c in range(len(img[0])):
            if img[r][c] == "#":
                new_r = len(list(filter(lambda x: r > x, rows_empty))) * factor + r
                new_c = len(list(filter(lambda x: c > x, cols_empty))) * factor + c
                gals.append((new_r, new_c))
    return gals

def part_1():
    gals = expand(FNAME, 2)
    tot = 0
    for (x1, y1), (x2, y2) in combinations(gals, 2):
        tot += abs(x2 - x1) + abs(y2 - y1)
    print(tot)

def part_2():
    gals = expand(FNAME, 1000000)
    tot = 0
    for (x1, y1), (x2, y2) in combinations(gals, 2):
        tot += abs(x2 - x1) + abs(y2 - y1)
    print(tot)

part_1()
part_2()