import regex as re
from math import lcm

def reader(fname, parse=False):
    res = "" if not parse else {}
    with open(fname, "r") as f:
        for line in f:
            if parse:
                n, lr = line.split("=")
                n = n.strip()
                lr = tuple(re.findall(r"[A-Z0-9]{3}", lr))
                res[n] = lr
            else:
                res += line
    return res
nodes = reader("nodes.txt", parse=True)
dirs = reader("dir.txt")

def part_1():
    steps = 0
    curr = "AAA"
    end = "ZZZ"
    while (curr != end):
        for dir in dirs:
            if curr == end:
                break
            elif dir == "L":
                curr = nodes[curr][0]
            else:
                curr = nodes[curr][1]
            steps += 1
    print(steps)

def part_2():
    steps = []
    tracks = list(filter(lambda x: x.endswith("A"), nodes.keys()))
    for track in tracks:
        step = 0
        while not track.endswith("Z"):
            for dir in dirs:
                if track.endswith("Z"):
                    break
                else:
                    idx = 1 if dir == "R" else 0
                    track = nodes[track][idx]
                    step += 1
        steps.append(step)
    print(lcm(*steps))

if __name__ == "__main__":
    part_1()
    part_2()