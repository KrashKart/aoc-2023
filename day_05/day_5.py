import regex as re
labels = ["seeds", "seed_soil", "soil_fertilizer", "fertilizer_water", "water_light", "light_temp", "temp_humidity", "humidity_location"]

def part_1(): 
    with open("day_5.txt", "r") as f:
        rows = {}
        local = []
        counter = 0
        for line in f:
            if line == "\n":
                continue
            elif "map" in line:
                rows[labels[counter]] = local
                local = []
                counter += 1
            elif "seeds" in line:
                entry = line.split(":")[1].strip().split(" ")
                local = list(map(lambda x: int(x), entry))
            else:
                entry = line.strip().split(" ")
                local.append(tuple(map(lambda x: int(x), entry)))
        rows[labels[counter]] = local
    counter = 1
    seeds = rows["seeds"]
    while counter < len(labels):
        for idx, seed in enumerate(seeds):
            for (dest, src, ran) in rows[labels[counter]]:
                if src <= seed < src + ran:
                    new_seed = seed - src + dest
                    seeds[idx] = new_seed
        counter += 1
    print(min(seeds))

def part_2():
    with open("day_5.txt", "r") as f:
        rows = {}
        local = []
        counter = 0
        for line in f:
            if line == "\n":      
                continue
            elif "map" in line:
                rows[labels[counter]] = local
                local = []
                counter += 1
            elif "seeds" in line:
                entry = re.findall(r"\d+ \d+", line)
                entry = list(map(lambda x: tuple(map(lambda x: int(x), x.split(" "))), entry))
                local = entry
            else:
                entry = line.strip().split(" ")
                local.append(tuple(map(lambda x: int(x), entry)))
        rows[labels[counter]] = local
    counter = 1
    
    seeds = rows["seeds"]
    while counter < len(labels):
        for idx, item in enumerate(seeds):
            start = item[0]
            rang = item[1]
            for (dest, src, ran) in rows[labels[counter]]:
                if start >= src + ran or start + ran < src:
                    continue
                else:
                    if rang == 0:
                        if src <= start < src + ran:
                            seeds[idx] = start - src + dest
                        else:
                            seeds.remove(item) 
                    elif src <= start < src + ran:
                        if start + rang >= src + ran:
                            seeds[idx] = (start - src + dest, src + ran - start) 
                            seeds.append((src + ran, start + rang - src - ran))
                        else:
                            seeds[idx] = (start - src + dest, rang)
                    elif start < src:
                        if src <= start + rang < src + ran:
                            seeds[idx] = (start, src - start - 1)
                            seeds.append((dest, start + rang - src))
                        elif start + rang >= src + ran:
                            seeds[idx] = (start, src - start - 1)
                            seeds.append((dest, ran))
                            seeds.append((src + ran, rang - (src - start - 1) - ran))
                    break
        counter += 1
    final = list(map(lambda x: x[0], seeds))
    print(min(final))

if __name__ == "__main__":
    part_1()
    part_2()
