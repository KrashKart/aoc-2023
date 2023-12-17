import heapq

FNAME = "day_17.txt"

m = []
with open(FNAME, "r") as f:
    for line in f:
        line = list(line.strip())
        m.append(list(map(int, line)))

possibles = {(1,0), (0,1), (-1,0), (0,-1)}

# credits to u/xelf for the very very heavy inspiration
def traverse(step, most):
    q = [(0, 0, 0, 0, 0)]
    visited = set()
    while q:
        tot, i, j, di, dj = heapq.heappop(q)
        if i == len(m) - 1 and j == len(m[0]) - 1:
            return tot
        elif (i, j, di, dj) in visited: 
            continue
        visited.add((i, j, di, dj))
        leftover = possibles - {(di, dj), (-di, -dj)}

        for ddi, ddj in leftover:
            tempt, tempi, tempj = tot, i, j
            for steps in range(1, most + 1):
                tempi, tempj = tempi + ddi, tempj + ddj
                if 0 <= tempi < len(m) and 0 <= tempj < len(m[0]):
                    tempt += m[tempi][tempj]
                    if steps >= step:
                        heapq.heappush(q, (tempt, tempi, tempj, ddi, ddj))

def part_1():
    print(traverse(1, 3))

def part_2():
    print(traverse(4, 10))

part_1()
part_2()