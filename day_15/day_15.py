chars = []
FNAME = "day_15.txt"

with open(FNAME, "r") as f:
    for line in f:
        chars = line.strip().split(",")

def hash(chars):
    char_sum = 0
    for c in chars:
        char_sum += ord(c)
        char_sum *= 17
        char_sum %= 256
    return char_sum

def part_1():
    tot = 0
    for char in chars:
        tot += hash(char)
    print(tot)

def part_2():
    boxes = {i: [] for i in range(256)}
    for char in chars:
        if "=" in char:
            s, focal = char.split("=")
            idx = hash(s)
            if s in list(map(lambda x: x[0], boxes[idx])):
                for i, pair in enumerate(boxes[idx]):
                    if pair[0] == s:
                        boxes[idx][i] = (s, int(focal))
                        break
            else:
                boxes[idx].append((s, int(focal)))
        else:
            s, _ = char.split("-")
            idx = hash(s)
            for pair in boxes[idx]:
                if pair[0] == s:
                    boxes[idx].remove(pair)
    tot = 0
    for i in range(256):
        if not boxes[i]:
            continue
        else:
            order = 1
            num = 0
            for pair in boxes[i]:
                num += (1 + i) * order * pair[1]
                order += 1
        tot += num
    print(tot)

part_1()
part_2()
