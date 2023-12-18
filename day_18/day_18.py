
dirs = []

FNAME = "day_18.txt"
with open(FNAME, "r") as f:
    for line in f:
        d, n, col = line.strip().split(" ")
        dirs.append((d, int(n), col))

ds = {"U": (-1,0), "D": (1,0), "L": (0,-1), "R": (0,1)}
dss = {0: "R", 1: "D", 2: "L", 3: "U"}

def shoelace(verts):
    iss, jss = [i for i, j in verts], [j for i, j in verts]
    a, b = 0, 0
    for c in range(1, len(jss)):
        a += iss[c-1] * jss[c]
        b += iss[c] * jss[c-1]
    a += iss[-1] * jss[0]
    b += iss[0] * jss[-1]
    return 0.5 * abs(a - b)

def part_1():
    edges = 0
    i, j = 0, 0
    verts = [(0, 0)]
    for (d, n, col) in dirs:
        di, dj = ds[d]
        i = i + di * n
        j = j + dj * n
        edges += n
        verts.append((i, j))
    print(int(shoelace(verts) + edges / 2 + 1))

def part_2():
    edges = 0
    i, j = 0, 0
    verts = [(0, 0)]
    for (_, _, col) in dirs:
        n, d = int(col[2:7], 16), int(col[-2])
        di, dj = ds[dss[d]]
        i = i + di * n
        j = j + dj * n
        edges += n
        verts.append((i, j))
    print(int(shoelace(verts) + edges / 2 + 1))
    
part_1()
part_2()