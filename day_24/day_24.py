FNAME = "day_24.txt"

hails = []
with open(FNAME, "r") as f:
    for line in f:
        poses, vels = line.strip().split(" @ ")
        px, py, pz = list(map(int, poses.split(", ")))
        vx, vy, vz = list(map(int, vels.split(", ")))
        hails.append((px, py, pz, vx, vy, vz))

def intersect(hail1, hail2, low_bound, upp_bound):
    px1, py1, _, vx1, vy1, _ = hail1
    px2, py2, _, vx2, vy2, _ = hail2
    m1, m2 = vy1 / vx1, vy2 / vx2
    if m1 == m2:
        return False
    else:
        x = (vx1 * vx2 * (py2 - py1) + vy1 * vx2 * px1 - vy2 * vx1 * px2) / (vy1 * vx2- vy2 * vx1)
        y = (vy1 * vy2 * (px2 - px1) + vx1 * vy2 * py1 - vx2 * vy1 * py2) / (vx1 * vy2- vx2 * vy1)
        deltax1, deltax2, deltay1, deltay2 = x - px1, x - px2, y - py1, y - py2
        if not low_bound <= x <= upp_bound or not low_bound <= y <= upp_bound:
            return False
        elif (vx1 != 0 and deltax1 / vx1 < 0) or (vx2 != 0 and deltax2 / vx2 < 0) or (vy1 != 0 and deltay1 / vy1 < 0) or (vy2 != 0 and deltay2 / vy2 < 0):
            return False
        else:
            return True

def part_1():
    count = 0
    LOW_BOUND, UPP_BOUND = 200000000000000, 400000000000000
    for i in range(len(hails) - 1):
        for j in range(i+1, len(hails)):
            if intersect(hails[i], hails[j], LOW_BOUND, UPP_BOUND):
                count += 1
    print(count)

part_1()