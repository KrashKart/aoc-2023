import copy

FNAME = "day_14.txt"

def load_dish():
    dish = []
    with open(FNAME, "r") as f:
        for line in f:
            line = list(line.strip())
            dish.append(line)
    return dish

def swap(dish, i, j, k, l):
    dish[i][j], dish[k][l] = dish[k][l], dish[i][j]

def north(dish):
    for i in range(1, len(dish)):
        for j in range(len(dish[0])):
            if dish[i][j] == "O":
                idx = i - 1
                pointer = dish[idx][j]
                while idx >= 0 and pointer == ".":
                    idx -= 1
                    pointer = dish[idx][j]
                idx += 1
                swap(dish, i, j, idx, j)
    return dish

def spin(dish):
    # north
    for i in range(1, len(dish)):
        for j in range(len(dish[0])):
            if dish[i][j] == "O":
                idx = i - 1
                pointer = dish[idx][j]
                while idx >= 0 and pointer == ".":
                    idx -= 1
                    pointer = dish[idx][j]
                idx += 1
                swap(dish, i, j, idx, j)
    
    # west
    for i in range(len(dish)):
        for j in range(1, len(dish[0])):
            if dish[i][j] == "O":
                idx = j - 1
                pointer = dish[i][idx]
                while idx >= 0 and pointer == ".":
                    idx -= 1
                    pointer = dish[i][idx]
                idx += 1
                swap(dish, i, j, i, idx)
    
    # south
    for i in range(len(dish) - 2, -1, -1):
        for j in range(len(dish[0])):
            if dish[i][j] == "O":
                idx = i + 1
                pointer = dish[idx][j]
                while idx < len(dish) - 1 and dish[idx][j] == ".":
                    idx += 1
                    pointer = dish[idx][j]
                idx -= 1 if pointer != "." else 0
                swap(dish, i, j, idx, j)
    
    # east
    for i in range(len(dish)):
        for j in range(len(dish[0]) - 2, -1, -1):
            if dish[i][j] == "O":
                idx = j + 1
                pointer = dish[i][idx]
                while idx < len(dish[0]) - 1 and dish[i][idx] == ".":
                    idx += 1
                    pointer = dish[i][idx]
                idx -= 1 if pointer != "." else 0
                swap(dish, i, j, i, idx)
    return dish

def part_1():
    dish_copy = load_dish()
    dish_copy = north(dish_copy)
    load = 0
    for i in range(len(dish_copy)):
        load += (len(dish_copy) - i) * dish_copy[i].count("O")
    print(load)

def part_2():
    dish = load_dish()
    visited = []
    while dish not in visited:
        visited.append(copy.deepcopy(dish))
        dish = spin(dish)
    target = visited.index(dish)
    dish = visited[(1000000000 - target) % (len(visited) - target) + target]
    
    load = 0
    for i in range(len(dish)):
        load += (len(dish) - i) * dish[i].count("O")
    print(load)

part_1()
part_2()