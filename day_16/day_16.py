grid = []
lase = []
from copy import deepcopy as dc
from collections import deque

FNAME = "day_16.txt"
with open(FNAME, "r") as f:
    for line in f:
        lase.append(list(map(lambda x: ".", line)))
        grid.append(list(line.strip()))
    
l = lambda x, y: (x,y-1)
u = lambda x, y: (x-1,y)
r = lambda x, y: (x,y+1)
d = lambda x, y: (x+1,y)
maps = {"/": {u: [r], l: [d], r: [u], d: [l]}, 
        "\\": {u: [l], l: [u], r: [d], d: [r]}, 
        "-": {u: [l, r], l: [l], r: [r], d: [l, r]}, 
        "|": {u: [u], l: [u, d], r: [u, d], d: [d]},
        ".": {u: [u], l: [l], r: [r], d: [d]}}

def traverse(grid, i_start, j_start, dir_start, laser):
    visited = []
    q = deque()
    q.append((i_start, j_start, dir_start))
    while q:
        i, j, dir = q.pop()
        if (i, j, dir) in visited:
            continue
        else:
            nextdirs = maps[grid[i][j]][dir]
            laser[i][j] = "#"
            for di in nextdirs:
                newi, newj = di(i, j)
                nextt = (newi, newj, di)
                if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]) and nextt not in q:
                    q.append(nextt)
            visited.append((i, j, dir))
    tot = 0
    for line in laser:
        tot += line.count("#")
    return tot

def part_1():
    g = dc(grid)
    la = dc(lase)
    print(traverse(g, 0, 0, r, la))

def part_2():
    max_j = len(grid[0]) - 1
    maxi = 0
    for i in range(len(grid)):
        print(i)
        if i == 0:
            for j in range(max_j):
                c, la = dc(grid), dc(lase)
                maxi = max(traverse(c, i, j, d, la), maxi)
        elif i == len(grid) - 1:
            for j in range(max_j):
                c, la = dc(grid), dc(lase)
                maxi = max(traverse(c, i, j, u, la), maxi)
        c1, l1 = dc(grid), dc(lase)
        c2, l2 = dc(grid), dc(lase)
        maxi = max(traverse(c1, i, 0, r, l1), maxi)
        maxi = max(traverse(c2, i, max_j, l, l2), maxi)
    print(maxi)  

part_1()
part_2()