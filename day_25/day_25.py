import networkx as xx
import random

FNAME = "day_25.txt"

g = xx.Graph()
with open(FNAME, "r") as f:
    for line in f:
        line = line.strip()
        main, others = line.split(': ')
        others = others.split(" ")
        for o in others:
            g.add_edge(main, o, capacity=1)

def part_1():
    cuts = 0
    while cuts != 3:
        nodes = list(g.nodes())
        one, two = random.choices(nodes, k=2)
        if one == two:
            continue
        else:
            cuts, partition = xx.minimum_cut(g, one, two)
    print(len(partition[0]) * len(partition[1]))

part_1()