from functools import cache
springs = []
records = []

FNAME = "day_12.txt"
with open(FNAME, "r") as f:
    for line in f:
        s, r = line.strip().split(" ")
        springs.append(s)
        groups = tuple(map(int, r.split(",")))
        records.append(groups)

@cache
def counter(line, grps, completed):
    if not line:
        return 1 if not grps and not completed else 0
    elif line[0] == "#":
        return counter(line[1:], grps, completed + 1)
    elif line[0] == ".":
        if grps and grps[0] == completed:
            return counter(line[1:], grps[1:], 0)
        elif completed == 0:
            return counter(line[1:], grps, 0)
        else:
            return 0
    else:
        return counter("#" + line[1:], grps, completed) + counter("." + line[1:], grps, completed)

def day_1():
    ways = 0
    for idx, line in enumerate(springs):
        ways += counter(line + ".", records[idx], 0)
    print(ways)

def day_2():
    ways = 0
    unfolded_s = list(map(lambda x: "?".join([x] * 5), springs))
    unfolded_recs = list(map(lambda x: x * 5, records))
    for idx, line in enumerate(unfolded_s):
        ways += counter(line + ".", unfolded_recs[idx], 0)
    print(ways)

day_1()
day_2()
