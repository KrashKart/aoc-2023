import regex as re

def part_1():
    def lookaround(master, row, start, end):
        urow = max(row - 1, 0)
        drow = min(row + 1, R - 1)
        le = max(0, start - 1)
        ri = min(C, end + 2)
        checklist = [master[r][c] for r in [urow, row, drow] for c in range(le, ri)]
        for sym in checklist:
            if sym in "!@#$%^&*()-=+_;:'/?><,":
                return int("".join(master[row][start:end + 1]))
        return 0

    with open("day_3.txt", "r") as f:
        master = []
        for l in f:
            master += [list(l.strip())]
    R = len(master)
    C = len(master[0])
    tot = 0
    numberClusters = []
    for i in range(R):
        j = 0
        while j < C:
            if not master[i][j].isdigit():
                j += 1
            else:
                cluster = [i, [j]]
                while (j < C and master[i][j].isdigit()):
                    j += 1
                cluster[1].append(j - 1)
                numberClusters.append(cluster)
    for clu in numberClusters:
        tot += lookaround(master, clu[0], clu[1][0], clu[1][1])
    print(tot)

def part_2():
    def count(master, row, col, numberClusters):
        urow = max(row - 1, 0)
        drow = min(row + 1, R - 1)
        ints = 0
        tot = 0
        for r in range(urow, drow + 1):
            checkrow = numberClusters[r]
            for pos in checkrow:
                if abs(col - pos[1]) <= 1 or abs(pos[0] - col) <= 1:
                    num = int("".join(master[r][pos[0]:pos[1] + 1]))
                    ints += 1
                    tot = num if tot == 0 else tot * num
        return 0 if ints != 2 else tot

    with open("day_3.txt", "r") as f:
        master = []
        for l in f:
            master += [list(l.strip())]
    R = len(master)
    C = len(master[0])
    tot = 0
    numberClusters = {}
    gears = []
    for i in range(R):
        j = 0
        while j < C:
            if master[i][j] == "*":
                gears.append([i, j])
                j += 1
            elif not master[i][j].isdigit():
                j += 1
            else:
                temp = j
                numberClusters[i] = numberClusters.get(i, [])
                while (j < C and master[i][j].isdigit()):
                    j += 1
                numberClusters[i].append([temp, j - 1])
    for g in gears:
        tot += count(master, g[0], g[1], numberClusters)
    print(tot)


if __name__ == "__main__":
    part_1()
    part_2()