import copy
maze = []
with open("day_10.txt", "r") as f:
    for idx, line in enumerate(f):
        if "S" in line:
            start = (idx, line.index("S"))
        line = list(line.strip())
        maze.append(line)

maze_copy = copy.deepcopy(maze)
def part_1():
    maxi = 1
    curr = (start[0] - 1, start[1])
    prev = start
    while maze[curr[0]][curr[1]] != "S":
        match maze[curr[0]][curr[1]]:
            case "|": nex = [(curr[0] - 1, curr[1]), (curr[0] + 1, curr[1])]
            case "7": nex = [(curr[0] + 1, curr[1]), (curr[0], curr[1] - 1)]
            case "J": nex = [(curr[0] - 1, curr[1]), (curr[0], curr[1] - 1)]
            case "-": nex = [(curr[0], curr[1] - 1), (curr[0], curr[1] + 1)]
            case "L": nex = [(curr[0] - 1, curr[1]), (curr[0], curr[1] + 1)]
            case "F": nex = [(curr[0] + 1, curr[1]), (curr[0], curr[1] + 1)]
        nex = list(filter(lambda x: x != prev, nex))[0]
        maze_copy[curr[0]][curr[1]] = maxi
        maxi += 1
        prev = curr
        curr = nex
    print(maxi // 2 if maxi % 2 == 0 else maxi // 2 + 1)

def part_2():
    sum = 0
    def count_nums(i, j):
        sum_nums = 0
        for jj in range(j):
            if maze[i][jj] in "|JLS" and isinstance(maze_copy[i][jj], int):
                sum_nums += 1
        return sum_nums % 2 == 1

    for i in range(1, len(maze)):
        for j in range(1, len(maze[0])):
            if not isinstance(maze_copy[i][j], int) and count_nums(i, j):
                sum += 1
    print(sum)

if __name__ == "__main__":
    part_1()
    part_2()