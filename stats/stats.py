import numpy as np
import matplotlib.pyplot as plt

one_rank = [14101, 25010, 11831, 6816, 32645, 7344]               # rank for part 1
two_rank = [11613, 24146, 10693, 7384, 16922, 5753]               # rank for part 2
two_stars_tot = [176441, 144108, 92084, 87971, 41786, 7905]       # number of people that completed both parts
add = [56863, 6446, 13896, 12127, 25195, 1762]                    # number of people that completed part 1 only
anomalies = [2, 5]                                          # days where I did not start on time

one_time = [(1,6,6), (3,44,38), (1,59,16), (0,18,0), (7,22,24), (0,22,7)]        # time taken for part 1 in (hrs, mins, secs)
two_time = [(2,3,32), (4,0,37), (2,34,4), (0,46,44), (8,38,27), (0,24,7)]        # time taken for part 2 in (hrs, mins, secs)
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
two_stars_tots = np.array(two_stars_tot, dtype=int)
totals_adds = two_stars_tots + np.array(add, dtype=int)
anoms = np.array(anomalies, dtype=int)
days = np.arange(start=1, stop=i, dtype=int)

Y_MIN = 0
Y_MAX_0 = max(totals_adds)
Y_MAX_1 = max(two_times)

fig, ax = plt.subplots(2, 1, figsize=(10, 15))
ax[0].plot(days, one_rank, "bo-", label="Part 1")
ax[0].plot(days, two_rank, "ro-", label="Part 2")
ax[0].plot(days, two_stars_tots, "g^--", label="Completion of Both Parts (Globally)")
ax[0].plot(days, totals_adds, "m*--", label="Completion of At Least 1 Part (Globally)")
ax[0].vlines(anoms, ymin=Y_MIN, ymax=Y_MAX_0, color="k", linestyles="dotted", label="Started late")
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
ax[1].set_title("Time taken (in mins) over Days")
ax[1].set_xlabel("Days")
ax[1].set_ylabel("Time (in mins)")
ax[1].legend(fontsize="small")
ax[1].grid(visible=True, which="major", axis="y")
ax[1].set_xticks(days)
ax[1].set_ylim(ymin=0)

plt.savefig("stat_of_the_day.png", format="png")
plt.show()