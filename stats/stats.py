import numpy as np
import matplotlib.pyplot as plt

# rank for part 1
one_rank = [14_101, 25_010, 11_831, 6_816, 32_645, 7_344, 15_939, 
            12_729, 48_507, 6_895, 22_213, 10_237]

# rank for part 2                
two_rank = [11_613, 24_146, 10_693, 7_384, 16_922, 5_753, 11_968, 
            8_778, 47_813, 3_266, 24_483, 3_930]

# number of people that completed both parts
two_stars_tot = [204_137, 171_552, 113_114, 111_911, 68_070, 86_521, 67_499, 
                 59_800, 59_639, 34_931, 38_888, 4_493]

# number of people that completed part 1 only
add = [64_750, 7_765, 16_784, 14_926, 26_311, 1_389, 5_907, 
       11_865, 837, 14_084, 1_929, 7_410]

# days where I did not start on time
anomalies = [2, 5, 7, 8, 9, 11, 12]

# days where I did not finish
DNF_2 = [10]

# time taken for part 1 in (hrs, mins, secs)
one_time = [(1,6,6), (3,44,38), (1,59,16), (0,18,0), (7,22,24), (0,22,7), (3,8,21), 
            (1,18,15), (0,19,0), (1,41,34), (1,15,0), (1,15,59)]       

# time taken for part 2 in (hrs, mins, secs)
two_time = [(2,3,32), (4,0,37), (2,34,4), (0,46,44), (8,38,27), (0,24,7), (3,8,29), 
            (1,59,59), (0,35,0), (2,26,53), (1,50,0), (1,27,13)]        
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
dnf = np.array(DNF_2, dtype=int)

Y_MIN = 0
Y_MAX_0 = max(totals_adds)
Y_MAX_1 = max(two_times)

fig, ax = plt.subplots(2, 1, figsize=(10, 15))
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