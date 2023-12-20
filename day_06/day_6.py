def calcways(totTime, rec):
        ways = 0
        for i in range(1, totTime + 1):
            d = i * (totTime - i)
            if d > rec:
                ways += 1
        return ways

def part_1():
    rows = []
    with open("day_6.txt", "r") as f:
        for line in f:
            rows.append(list(map(lambda x: int(x), line.split())))

    times = rows[0]
    dists = rows[1]
    ways = 1
    for i in range(len(times)):
        ways *= calcways(times[i], dists[i])
    print(ways)

def part_2():
    rows = []
    with open("day_6.txt", "r") as f:
        for line in f:
            rows.append(int("".join(line.split(" "))))
    times = rows[0]
    dists = rows[1]
    ways = calcways(times, dists)
    print(ways)

if __name__ == "__main__":
    part_1()
    part_2()