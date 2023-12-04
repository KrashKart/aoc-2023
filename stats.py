import numpy as np
import matplotlib.pyplot as plt

one_rank = [14101, 25010, 11831, 6816]
two_rank = [11613, 24146, 10693, 7384]
total = [154354, 120716, 72083, 36771]
add = [50180, 5364, 11757, 10872]

one_time = [(1,6,6), (3,44,38), (1,59,16), (0,18,0)]
two_time = [(2,3,32), (4,0,37), (2,34,4), (0,46,44)]
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
totals = np.array(total, dtype=int)
totals_adds = totals + np.array(add, dtype=int)
days = np.arange(start=1, stop=i, dtype=int)

fig, ax = plt.subplots(1, 2, figsize=(16, 6))
ax[0].plot(days, one_rank, "bo-", label="Part 1")
ax[0].plot(days, two_rank, "ro-", label="Part 2")
ax[0].plot(days, total, "g^--", label="Completion of Both Parts (Globally)")
ax[0].plot(days, totals_adds, "m*--", label="Completion of At Least 1 Part(Globally)")
ax[0].set_title("Rank (1 being first to complete) over Days")
ax[0].set_xlabel("Days")
ax[0].set_ylabel("Rank")
ax[0].legend(fontsize="small")
ax[0].grid(visible=True, which="major", axis="y")
ax[0].set_xticks(days)

ax[1].plot(days, one_time, "bo-", label="Part 1")
ax[1].plot(days, two_time, "ro-", label="Part 2")
ax[1].set_title("Time taken (in mins) over Days")
ax[1].set_xlabel("Days")
ax[1].set_ylabel("Time (in mins)")
ax[1].legend(fontsize="small")
ax[1].grid(visible=True, which="major", axis="y")
ax[1].set_xticks(days)

plt.show()

plt.savefig("stat_of_the_day", format="png")