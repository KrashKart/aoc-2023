seqs = []
with open("day_9.txt", "r") as f:
    for line in f:
        line = list(map(lambda x: int(x), line.split(" ")))
        seqs.append(line)

def part_1():
    def get_next(line):
        diffs = []
        rep = False
        for i in range(1, len(line)):
            if line[i] != line[i - 1]:
                rep = True
            diffs.append(line[i] - line[i - 1])
        return get_next(diffs) + line[-1] if rep else line[-1]
    
    sum = 0
    for seq in seqs:
        sum += get_next(seq)
    print(sum)

def part_2():
    def get_prev(line):
        diffs = []
        rep = False
        for i in range(len(line) - 1, 0, -1):
            if line[i] != line[i - 1]:
                rep = True
            diffs = [line[i] - line[i - 1]] + diffs
        return line[0] - get_prev(diffs) if rep else line[0]
    
    sum = 0
    for seq in seqs:
        sum += get_prev(seq)
    print(sum)

if __name__ == "__main__":
    part_1()
    part_2()