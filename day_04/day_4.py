import regex as re

def part_1():
    def count(line):
        tot = 0
        line = line.split(":")[1]
        splits = line.split("|")
        wins = re.findall(r"\d+", splits[0])
        ours = re.findall(r"\d+", splits[1])
        for num in ours:
            if num in wins:
                tot = 1 if tot == 0 else tot * 2
        return tot
    tot = 0
    with open("day_4.txt", "r") as f:
        for line in f:
            tot += count(line)
    print(tot)

def part_2():
    def count(line):
        tot = 0
        line = line.split(":")[1]
        splits = line.split("|")
        wins = re.findall(r"\d+", splits[0])
        ours = re.findall(r"\d+", splits[1])
        for num in ours:
            if num in wins:
                tot += 1
        return tot
    ref = []
    multi = []
    with open("day_4.txt", "r") as f:
        for line in f:
            idx = re.findall(r"Card +(\d+):", line)[0]
            ref.append((int(idx), line))
            multi.append(1)
    for idx, line in ref:
        nextls = count(line)
        for i in range(idx, min(len(ref), idx + nextls)):
            multi[i] += multi[idx - 1]
    print(sum(multi))

if __name__ == "__main__":
    part_1()
    part_2()