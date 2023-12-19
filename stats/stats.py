import numpy as np
import matplotlib.pyplot as plt

PLOT = True

# parser for ranktimes
one_rank, one_time, two_rank, two_time = [], [], [], []
with open("ranktimes.txt", "r") as f:
    for line in f:
        line = line.strip().split(" ")
        _, oT, oR, _, tT, tR, _ = list(filter(lambda x: x, line))
        one_rank.append(int(oR))
        two_rank.append(int(tR))
        oh, om, os = oT.strip().split(":")
        th, tm, ts = tT.strip().split(":")
        one_time.append((int(oh), int(om), int(os)))
        two_time.append((int(th), int(tm), int(ts)))

# parser for tots
two_stars_tots = []
add = []
with open("tots.txt", "r") as f:
    for line in f:
        line = line.strip().split(" ")
        _, t, a, _ = list(filter(lambda x: x, line))
        two_stars_tots.append(int(t))
        add.append(int(a))
for ls in [one_rank, one_time, two_rank, two_time, two_stars_tots, add]:
    ls.reverse()

# days where I did not start on time
anomalies = [2, 5, 7, 8, 9, 11, 12, 13, 14, 16, 17, 19]

# days where I did not finish
DNF_2 = [10]
   
i = len(one_rank) + 1

def convert_to_mins(tup):
    hours, mins, secs = tup
    return round(hours * 60 + mins + secs/60)

one_time = list(map(convert_to_mins, one_time))
two_time = list(map(convert_to_mins, two_time))

one_ranks = np.array(one_rank, dtype=int)
two_ranks = np.array(two_rank, dtype=int)
one_times = np.array(one_time)
two_times = np.array(two_time)
two_stars_tots = np.array(two_stars_tots, dtype=int)
totals_adds = two_stars_tots + np.array(add, dtype=int)
anoms = np.array(anomalies, dtype=int)
days = np.arange(start=1, stop=i, dtype=int)
dnf = np.array(DNF_2, dtype=int)

Y_MIN = 0
Y_MAX_0 = max(totals_adds)
Y_MAX_1 = max(two_times)

if PLOT:
    fig, ax = plt.subplots(2, 1, figsize=(15, 10))
    ax[0].plot(days, one_rank, "bo-", label="Part 1")
    ax[0].plot(days, two_rank, "ro-", label="Part 2")
    ax[0].plot(days, two_stars_tots, "g^--", label="Completion of Both Parts (Globally)")
    ax[0].plot(days, totals_adds, "m*--", label="Completion of At Least 1 Part (Globally)")
    ax[0].vlines(anoms, ymin=Y_MIN, ymax=Y_MAX_0, color="k", linestyles="dotted", label="Started late")
    ax[0].vlines(dnf, ymin=Y_MIN, ymax=Y_MAX_0, color="y", linestyle="dotted", label="Did not finish part 2")
    ax[0].set_title("Rank (1 being first to complete) over Days")
    ax[0].set_xlabel("Days")
    ax[0].set_ylabel("Rank")
    ax[0].legend(fontsize="small")
    ax[0].grid(visible=True, which="major", axis="y")
    ax[0].set_xticks(days)
    ax[0].set_ylim(ymin=0)

    ax[1].plot(days, one_time, "bo-", label="Part 1")
    ax[1].plot(days, two_time, "ro-", label="Part 2")
    ax[1].vlines(anoms, ymin=Y_MIN, ymax=Y_MAX_1, color="k", linestyles="dotted", label="Started late")
    ax[1].vlines(dnf, ymin=Y_MIN, ymax=Y_MAX_1, color="y", linestyle="dotted", label="Did not finish part 2")
    ax[1].set_title("Time taken (in mins) over Days")
    ax[1].set_xlabel("Days")
    ax[1].set_ylabel("Time (in mins)")
    ax[1].legend(fontsize="small")
    ax[1].grid(visible=True, which="major", axis="y")
    ax[1].set_xticks(days)
    ax[1].set_ylim(ymin=0)

    plt.savefig("stat_of_the_day.png", format="png")
    plt.show()