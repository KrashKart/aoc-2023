from collections import deque
from math import lcm

nodes = {}
q = deque()
H, L = 0, 0
FNAME = "day_20.txt"

class node:
    def __init__(self, name, dests):
        self.name = name
        self.dests = dests

class flip(node):
    def __init__(self, name, dests):
        super().__init__(name, dests)
        self.state = "off"

    def prop(self, name, pulse):
        global H, L, q
        if pulse == "low":
            self.state = "on" if self.state == "off" else "off"
            send = "high" if self.state == "on" else "low"
            for d in self.dests:
                if d not in nodes:
                    nodes[d] = final(d)
                q.append((d, self.name, send))
                H += 1 if send == "high" else 0
                L += 1 if send == "low" else 0

class conj(node):
    def __init__(self, name, dests):
        super().__init__(name, dests)
        self.froms = {}
        self.rmb = "low"

    def prop(self, name, pulse):
        global H, L, q
        self.froms[name] = pulse
        send = "low" if all(c == "high" for c in self.froms.values()) else "high"
        for d in self.dests:
            if d not in nodes:
                nodes[d] = final(d)
            q.append((d, self.name, send))
            H += 1 if send == "high" else 0
            L += 1 if send == "low" else 0
    
class broadcaster(node):
    def __init__(self, name, dests):
        super().__init__(name, dests)

    def prop(self):
        global L, q
        for d in self.dests:
            if d not in nodes:
                nodes[d] = final()
            q.append((d, self.name, "low"))
        L += len(self.dests) + 1

class final(node):
    def __init__(self, name):
        self.name = name

    def prop(self, name, pulse):
        return

conjs = []
with open(FNAME, "r") as f:
    for line in f:
        name, dests = line.strip().split(" -> ")
        dests = dests.split(", ")
        if name == "broadcaster":
            nodes[name] = broadcaster(name, dests)
        else:
            t, name = name[0], name[1:]
            if t == "%":
                nodes[name] = flip(name, dests)
            else:
                nodes[name] = conj(name, dests)
                conjs.append(name)

for n in nodes.keys():
    for d in nodes[n].dests:
        if d in conjs:
            nodes[d].froms[nodes[n].name] = "low"

def part_1():
    global H, L, q
    for _ in range(1000):
        nodes["broadcaster"].prop()
        while q:
            to, fro, send = q.popleft()
            nodes[to].prop(fro, send)
    print(H * L)

# rg inputs to rx
# kd, zf, vg, gs inputs to rg --> all must send high inputs to rg for low output to rx
periods = {}
def part_2():
    global state, q
    count = 0
    changed = 0
    while changed < 4:
        count += 1
        nodes["broadcaster"].prop()
        while q:
            to, fro, send = q.popleft()
            if to == "rg" and send == "high":
                if fro in periods.keys():
                    changed += 1
                periods[fro] = count - periods.get(fro, 0)
            nodes[to].prop(fro, send)
    print(lcm(*[p for p in periods.values()]))

part_1()
part_2()
