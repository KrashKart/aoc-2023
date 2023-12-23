import sys
from collections import defaultdict as dd
sys.setrecursionlimit(1000000)
FNAME = "day_23.txt"

grid = []
with open(FNAME, "r") as f:
    for idx, line in enumerate(f):
        line = list(line.strip())
        if line.count(".") == 1:
            if idx == 0:
                si, sj = idx, line.index(".")
            else:
                ei, ej = idx, line.index(".")
        grid.append(line)

def nexts(curr, part):
    i, j = curr
    adjs = {"^": (-1,0), ">": (0,1), "v": (1,0), "<": (0,-1)}
    if part == 1 and grid[i][j] in "^>v<":
        adjs = {"haha": adjs[grid[i][j]]}
    possible = []
    adjs = adjs.values()
    for di, dj in adjs:
        nexti, nextj = i + di, j + dj
        if 0 <= nexti < len(grid) and 0 <= nextj < len(grid[0]) and grid[nexti][nextj] != "#":
            possible.append((nexti, nextj))
    return possible

def dfs(curr, visited, dist, part, g=None):
    if curr == (ei, ej):
        return dist
    maxi = 0
    if part == 1:
        for nn in nexts(curr, 1):
            if nn not in visited:
                maxi = max(dfs(nn, visited + [nn], dist + 1, part), maxi)
    else:
        for d, nn in g[curr]:
            if nn not in visited:
                maxi = max(dfs(nn, visited + [nn], dist + d, part, g), maxi)
    return maxi

def condense(grid):
    g = dd(list)
    v = {(si, sj), (ei, ej)}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "#":
                if len(list(nexts((i, j), 2))) > 2:
                    v.add((i, j))

    for i, j in v:
        q, visited, dist = [(i, j)], {(i, j)}, 0
        while q:
            nex = []
            dist += 1
            for c in q:
                for a in nexts(c, 2):
                    if a not in visited:
                        if a in v:
                            g[(i, j)].append((dist, a))
                        else:
                            nex.append(a)
                        visited.add(a)
            q = nex
    return g

def part_1():
    print(dfs((si, sj), [], 0, 1))

def part_2():
    g = condense(grid)
    print(dfs((si, sj), [], 0, 2, g))

part_1()
part_2()