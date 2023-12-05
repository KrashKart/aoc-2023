file = open('day_5.txt','r')
lst = [i.strip() for i in file]

seeds = [int(i) for i in lst[0].split(": ")[1].split(" ")]
maps = []
for line in lst[2:]:
    if not line:
        continue
    if 'map' in line:
        mapper = []
        maps.append(mapper)
    else:
        mapper.append([int(i) for i in line.split(" ")])

# # Part 1

# score = 1000000000000000000000000000000000000000000000
# for seed in seeds:
#     temp = seed
#     for m in maps:
#         for d,s,r in m:
#             if s <= temp <= s+r-1:
#                 temp += d-s
#                 break
#     score = min(temp,score)
# #print(score)

# Part 2

seeds2 = [(seeds[2*i],seeds[2*i+1]) for i in range(len(seeds)//2)]
score2 = 0
flag2 = True
while flag2:
    temp = score2
    for m in maps[::-1]:
        for d,s,r in m:
            if d <= temp <= d+r-1:
                temp += s-d
                break
    flag = True
    for i,j in seeds2:
        if i <= temp <= i+j-1:
            flag = False
            break
    if flag:
        score2 += 1
    else:
        print(score2)
        break