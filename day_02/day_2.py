import regex as re

def part_1():
    RED = 12
    GREEN = 13
    BLUE = 14

    def verify(line):
        r = re.findall(r"(\d+) red", line)
        g = re.findall(r"(\d+) green", line)
        b = re.findall(r"(\d+) blue", line)

        r = 0 if not r else max(map(lambda x: int(x), r))
        g = 0 if not g else max(map(lambda x: int(x), g))
        b = 0 if not b else max(map(lambda x: int(x), b))

        if r > RED or g > GREEN or b > BLUE:
            return 0
        id = re.search(r"Game (\d+):", line)
        return int(id[1])
    
    tot = 0
    with open("day_2.txt", "r") as f:
        for l in f:
            tot += verify(l)
    print(f"Final part 1: {tot}")

def part_2():
    def power(line):
        r = re.findall(r"(\d+) red", line)
        g = re.findall(r"(\d+) green", line)
        b = re.findall(r"(\d+) blue", line)

        r = 0 if not r else max(map(lambda x: int(x), r))
        g = 0 if not g else max(map(lambda x: int(x), g))
        b = 0 if not b else max(map(lambda x: int(x), b))
        
        return r * g * b
    
    tot = 0
    with open("day_2.txt", "r") as f:
        for l in f:
            tot += power(l)
    print(f"Final part 2: {tot}")

if __name__ == "__main__":
    part_1()
    part_2()