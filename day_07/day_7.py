from collections import Counter

def part_1():
    cards = "23456789TJQKA"
    vals = {c: cards.index(c) for c in cards}
    def ranker(hand, amt):
        hander= dict(Counter(hand))
        to_attach = (hand, amt)
        if len(hander) == 1:
            rankings[7].append(to_attach)
        elif len(hander) == 2:
            for val in hander.values():
                if val == 4:
                    rankings[6].append(to_attach)
                    break
                elif val == 3 or val == 2:
                    rankings[5].append(to_attach)
                    break
        elif len(hander) == 3:
            for val in hander.values():
                if val == 3:
                    rankings[4].append(to_attach)
                    break
                elif val == 2:
                    rankings[3].append(to_attach)
                    break
        elif len(hander) == 4:
            rankings[2].append(to_attach)
        else:
            rankings[1].append(to_attach)

    rankings = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
    with open("day_7.txt", "r") as f:
        for line in f:
            hand, amt = line.strip().split(" ")
            ranker(hand, amt)
    
    sum = 0
    cum = 0
    for i in range(1, 8):
        l = sorted(rankings[i], key=lambda x: [vals[c] for c in x[0]])
        for e in l:
            sum += int(e[1]) * (l.index(e) + 1 + cum)
        cum += len(l)
    print(sum)

def part_2():
    j_cards = "J23456789TQKA"
    j_vals = {c: j_cards.index(c) for c in j_cards}

    def ranker_2(hand, amt):
        hander= dict(Counter(hand))
        to_attach = (hand, amt)
        if "J" in hander.keys() and len(hander.keys()) > 1:
            adder = hander["J"]
            del hander["J"]
            replace = max(hander, key=lambda x: (hander[x], j_vals[x]))
            hander[replace] += adder

        if len(hander) == 1:
            rankings[7].append(to_attach)
        elif len(hander) == 2:
            for val in hander.values():
                if val == 4:
                    rankings[6].append(to_attach)
                    break
                elif val == 3 or val == 2:
                    rankings[5].append(to_attach)
                    break
        elif len(hander) == 3:
            for val in hander.values():
                if val == 3:
                    rankings[4].append(to_attach)
                    break
                elif val == 2:
                    rankings[3].append(to_attach)
                    break
        elif len(hander) == 4:
            rankings[2].append(to_attach)
        else:
            rankings[1].append(to_attach)

    rankings = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
    with open("day_7.txt", "r") as f:
        for line in f:
            hand, amt = line.strip().split(" ")
            ranker_2(hand, amt)
    
    sum = 0
    cum = 0
    for i in range(1, 8):
        l = sorted(rankings[i], key=lambda x: [j_vals[c] for c in x[0]])
        for e in l:
            sum += int(e[1]) * (l.index(e) + 1 + cum)
        cum += len(l)
    print(sum)


if __name__ == "__main__": 
    part_1()
    part_2()
