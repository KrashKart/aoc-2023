maze = []
with open("day_10.txt", "r") as f:
    for idx, line in enumerate(f):
        if "S" in line:
            start = (idx, line.index("S"))
            line = line.replace("S", "J")
        line = list(line.strip())
        maze.append(line)

dirs = {"|": lambda di,dj: (di,dj), "-": lambda di,dj: (di,dj), 
        "7": lambda di,dj: (dj,di), "F": lambda di,dj: (-dj,-di),
        "L": lambda di,dj: (dj,di), "J": lambda di,dj: (-dj,-di)}

def part_1():
    visited = []
    num = -1
    i, j = start
    di, dj = -1,0
    while (i, j) not in visited:
        visited.append((i, j))
        i, j = i + di, j + dj
        num += 1
        di, dj = dirs[maze[i][j]](di, dj)
    print(num / 2 if num % 2 == 0 else num // 2 + 1)

def shoelace(verts):
    iss, jss = [i for i, j in verts], [j for i, j in verts]
    a, b = 0, 0
    for c in range(1, len(jss)):
        a += iss[c-1] * jss[c]
        b += iss[c] * jss[c-1]
    a += iss[-1] * jss[0]
    b += iss[0] * jss[-1]
    return 0.5 * abs(a - b)

def part_2():
    visited = []
    verts = []
    i, j = start
    di, dj = -1,0
    num = 0
    while (i, j) not in visited:
        visited.append((i, j))
        if maze[i][j] in "J7FL":
            verts.append((i, j))
        i, j = i + di, j + dj
        di, dj = dirs[maze[i][j]](di, dj)
        num += 1
    print(int(shoelace(verts) - num / 2 + 1))
    
if __name__ == "__main__":
    part_1()
    part_2()