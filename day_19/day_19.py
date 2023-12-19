WORKFLOW = "workflows.txt"
PARTS = "parts.txt"

from copy import deepcopy as dc

flows = {}
parts = []

def lt(a, b):
    return a < b

def gt(a, b):
    return a > b

class comp:
    def __init__(self, crits):
        ff = []
        self.ranges = []
        for c in crits:
            if ":" in c:
                pred, res = c.split(":")
                sym = "<" if "<" in pred else ">"
                var, val = pred.split(sym)
                op = lt if "<" in pred else gt
                ff.append((op, var, int(val), res))
                self.ranges.append((sym, var, int(val), res))
            else:
                first = lambda _: c
                final = c
        self.crits = list(map(lambda w: lambda l: w[3] if w[0](l[w[1]], w[2]) else "pppp", ff))
        self.crits.append(first)
        self.ranges.append(("final", final, final, final))
    
    def eval(self, item):
        counter = 0
        res = "pppp"
        while res == "pppp":
            res = self.crits[counter](item)
            counter += 1
        return res

with open(WORKFLOW, "r") as f:
    for line in f:
        line = line.strip().strip("}")
        name, criteria = line.split("{")
        flows[name] = comp(criteria.split(","))

with open(PARTS, "r") as f:
    for line in f:
        line = line.strip()[1:-1]
        line = line.split(",")
        curr = dict()
        for v in line:
            var, val = v.strip().split("=")
            curr[var] = int(val)
        parts.append(curr)

def part_1():
    tot = 0
    for part in parts:
        res = flows["in"].eval(part)
        while res not in "AR":
            res = flows[res].eval(part)
        if res == "A":
            for c in "xmas":
                tot += part[c]
    print(tot)

def traverse(curr, xmas):
    if curr == "R":
        return 0
    elif curr == "A":
        xs = xmas["x"][1] - xmas["x"][0] + 1
        ms = xmas["m"][1] - xmas["m"][0] + 1
        aas = xmas["a"][1] - xmas["a"][0] + 1
        ss = xmas["s"][1] - xmas["s"][0] + 1
        return xs * ms * aas * ss 
    else:
        tot = 0
        comper = flows[curr].ranges
        for (sym, var, val, res) in comper:
            if sym == "final":
                tot += traverse(res, xmas)
            else:
                if (sym == ">" and xmas[var][0] > val) or (sym == "<" and xmas[var][1] < val):
                    tot += traverse(res, xmas)
                else:
                    xmas_new = dc(xmas)
                    if xmas[var][0] < val < xmas[var][1]:
                        if sym == "<":
                            xmas_new[var] = (xmas[var][0], val - 1)
                            xmas[var] = (val, xmas[var][1])
                        else:
                            xmas_new[var]  = (val + 1, xmas[var][1])
                            xmas[var] = (xmas[var][0], val)
                        tot += traverse(res, xmas_new)
    return tot

def part_2():
    start = {"x": (1, 4000), "m": (1, 4000), "a": (1,4000), "s":(1,4000)}
    print(traverse("in", start))
    
part_1()
part_2()