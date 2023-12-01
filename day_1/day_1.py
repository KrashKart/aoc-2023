# part 1
import regex as re
def part_1():
    sum1 = 0
    def extract_1(line):
        nums = re.findall(r"[1-9]", line)
        num = int(nums[0]) * 10 + int(nums[-1])
        return num
    with open("aoc_day_1.txt", "r") as f:
        for line in f:
            sum1 += extract_1(line)
    print(sum1)

# part 2
def part_2():
    def extract_2(line):
        ref = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        stuff = re.findall(r"[1-9]|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True)
        first = int(stuff[0]) if stuff[0].isnumeric() else ref[stuff[0]]
        last = int(stuff[-1]) if stuff[-1].isnumeric() else ref[stuff[-1]]
        return first * 10 + last
    sum2 = 0
    with open("aoc_day_1.txt", "r") as f:
        for line in f:
            sum2 += extract_2(line)
    print(sum2)


if __name__ == "__main__":
    part_1()
    part_2()