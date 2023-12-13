diags = []
FNAME = "day_13.txt"
with open(FNAME, "r") as f:
    diag = []
    for line in f:
        if line == "\n":
            diags.append(diag)
            diag = []
        else:
            diag.append(line.strip())

def check_height(diag, diff):
    for i in range(len(diag) - 1):
        d = str_diff(diag[i], diag[i + 1]) # see whether a line between rows is a mirror
        smudged = False # check smudge
        if d == 1:
            if diff == 0: # if no smudges allowed, move to next line
                continue
            else:
                smudged = True # else, count the smudge
        if d <= 1:
            s = i - 1 # check the next pair
            e = i + 2
            while 0 <= s and e < len(diag): 
                d = str_diff(diag[s], diag[e])
                if d != 0 and diff == 0: # if next rows dont match, skip to check next line
                    break
                elif d > 1 or (d == 1 and smudged): # if more than 1 smudge is required, skip and check next line
                    break
                elif d == 1: # count smudge, but proceed
                    smudged = True
                e += 1
                s -= 1
            else: 
                if not smudged and diff == 1: # checks to ensure a different line is used for part 2
                    continue
                return i + 1

def transpose(x):
        # stole this off the reddit lol
	    return list(map("".join, zip(*x)))

def score(diag, diff):
    h = check_height(diag, diff)
    return 100 * h if h else check_height(transpose(diag), diff)

def str_diff(str1, str2):
    sums = 0
    for c1, c2 in zip(list(str1), list(str2)):
        if c1 != c2:
            sums += 1
    return sums

def part_1():
    sums = 0
    for diag in diags:
        sums += score(diag, 0)
    print(sums)

def part_2():
    sums = 0
    for diag in diags:
        sums += score(diag, 1)
    print(sums)

part_1()
part_2()