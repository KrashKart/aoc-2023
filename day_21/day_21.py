FNAME = "day_21.txt"
grid = []

with open(FNAME, "r") as f:
    for idx, line in enumerate(f):
        if "S" in line:
            si, sj = (idx, line.index("S"))
        grid.append(list(line.strip()))

def traverse(si, sj, steps):
    n, m = len(grid), len(grid[0])
    ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    boundary = {(si, sj)}
    for _ in range(1, steps + 1):
        visited = set()
        for i, j in boundary:
            for (di, dj) in ds:
                newi, newj = i + di, j + dj
                if grid[newi % n][newj % m] != "#": # wrap around
                    visited.add((newi, newj))
        boundary = visited
    return len(boundary)

def f(*y, s):
    y0, y1, y2 = y
    return y0 + (y1 - y0) * s + (y2 - y1 - y1 + y0)//2 * s * (s - 1)

def part_1():
    steps = 64
    print(traverse(si, sj, steps))

def part_2():
    steps = 26501365
    r, l = steps % 131, 131

    # compute first 3 values of n, n + l and n + 2l
    p, q, r = traverse(si, sj, r), traverse(si, sj, r + l), traverse(si, sj, r + 2 * l)
    print(f(p, q, r, s = steps // 131))

part_1()
part_2()