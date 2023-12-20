# Overview
Hello, welcome to my AOC 2023 repo, where I post my solutions, problem data and test cases. I decided to challenge myself to complete the daily tasks to improve my coding skills and programmatic thinking.

# What is AOC?
For those unfamiliar, AOC an Advent of Code, where in the style of an advent calendar, code challenges are released everyday at 1pm Singapore Time (midnight EST or UTC-5). A problem description and problem data (in the form of text) will be given, and the solution must be entered below the problem description. 

There are 2 tiers of problems per day, Part 1 and Part 2, which is a harder extension of Part 1 and unlocks only after completion of Part 1. Any wrong answer will come with a 1 minute wait time (which increases after a certain amount of wrong answers) before an answer can be submitted, along with a hint whether the answer is too high or low. 

Completion of Part 1 yields 1 star (silver), and that of both parts yields 2 (gold). There are no restrictions on programming languages, and the time taken since the release of the problem set will be used in the global leaderboard and any private leaderboards you are registered in.

I chose to do my coding in Python 3.11. These solutions are definitely not the most efficient, but I try to make them as short and concise as possible.

Huge thanks to the creator of AOC, [Eric Wastl](http://was.tl/).

[View the AOC 2023 page here](https://adventofcode.com/2023/about)

# Days and Reflections
1.  [Trebuchet?](https://adventofcode.com/2023/day/1) (2/2 stars)
    * This was a particularly difficult day 1 from what I heard in my university discord, which I agree. I expected it to be trivial but it ended up costing me 2 hours...
2.  [Cube Conundrum](https://adventofcode.com/2023/day/2) (2/2 stars)
    * This was manageable, but my string processing was quite weak so fumbled on the regex considerably.
3.  [Gear Ratios](https://adventofcode.com/2023/day/3) (2/2 stars)
    * This problem seemed tedious at first. I eventually opted to store each character in an n x n array, recording the indices of the groups of numbers and symbols that were not ".", and traversed the entire n x n array
4.  [Scratchcards](https://adventofcode.com/2023/day/4) (2/2 stars)
    * Very manageable actually. Solved this one quite quickly due to me being used to regex. I opted for a "bottom-up" style of dynamic programming in Part 2 which if not for a careless mistake, could've been my first sub-20 minute submission.
5.  [If You Give A Seed A Fertilizer](https://adventofcode.com/2023/day/5) (2/2 stars)
    * This was slightly complicated to wrap my head around. My approach was a more mathematical and logical one in part 2 as compared to my initial idea which was brute-forcing.
6.  [Wait For It](https://adventofcode.com/2023/day/6) (2/2 stars)
    * A particularly easy day, even easier than day 4. The input text was not lengthy at all, so any tricky edge cases were not included. I chose to brute force search my way through.
7.  [Camel Cards](https://adventofcode.com/2023/day/7) (2/2 stars)
    * A fantastic problem of ranking poker combinations. I did not use regex and instead opted for the Collections module as suggested in my university Discord. I must disclose that I knew about the problem before I opened it (but after the leaderboard was already filled) thus my completion times were quite sus.
8.  [Haunted Wasteland](https://adventofcode.com/2023/day/8) (2/2 stars)
    * I was undaunted initially because I had solved several node-pathfinding problems on LeetCode before, thus part 1 didn't require too much thinking. For part 2, I messed up my order of execution of functions, and coupled with my initial idea to brute force (which failed due to the large magnitude of the answer), this caused a delay in solving part 2. I managed to figure out an alternative, faster solution in the form of the lcm function in the math module.
9.  [Mirage Maintenance](https://adventofcode.com/2023/day/9) (2/2 stars)
    * Quite an easy series puzzle. I started on this on day 10 as I was busy but completed it in less than 45 minutes
10. [Pipe Maze](https://adventofcode.com/2023/day/10) (2/2 stars)
    * Initially, when I first did this I was unaware of the di, dj navigation system, the Shoelace Formula or Pick's Theorem, so I had to find an answer online.
    * Having done day 18, I finally learnt all of the above, allowing me to craft a clean algorithm for traversal and calculation of the internal area. The only twist was that I had to subtract half the number of edges for Pick's Theorem as only the internal area excluding the edges was required. I figured Pick's Theorem did include half the area bounded by the edge tiles, and I added 1 to account for the problem described in day 18 regarding internal and external corners.
11. [Cosmic Expansion](https://adventofcode.com/2023/day/11) (2/2 stars)
    * I misread the question so I thought it was harder than it really was, but it was a relatively simple problem which I managed to figure out quickly once I ironed out implementation mistakes. I've been starting to think more mathematically rather than brute-forcing-ly so I guess that is good too.
    * Also, AOC has been training me to use itertools and other libraries in Python more often, which I really appreciate.
12. [Hot Springs](https://adventofcode.com/2023/day/12) (2/2 stars)
    * An interesting Dynamic Programming problem. This introduced me to the @cache decorator in functools and how to memoize in Python. I only understood how to do this after reading a hint on the reddit, but nonetheless quite proud of my solution (although it could be better)
13. [Point of Incidence](https://adventofcode.com/2023/day/13) (2/2 stars)
    * I was stuck initially because I tried to use maths to figure out the middle, but I realised that I could just try every line between each row to see which one the middle was.
    * Part 2 was simply to refactor my check_height() function to account for smidges, which did not take long.
14. [Parabolic Reflector Dish](https://adventofcode.com/2023/day/14) (2/2 stars)
    * A rather simple problem. As usual I had several off-by-one errors but managed to complete it within the 90 minute mark. I appreciated the subtle twist in the cycle detection algorithm required in part 2 as I didn't realise a cycle could occur until I got a hint from the Discord. I realised too that rather than implementing the hare and tortoise traversal algorithm I could just generate the spins and check if it had occured before, and take that as the start of the loop.
15. [Lens Library](https://adventofcode.com/2023/day/15) (2/2 stars)
    * Another simple problem (thank you Eric). An interesting introduction to simple hashing algorithms (reminiscent of SHA256). Beyond that it was more a reading problem (skill issue on my part tbh) than a coding problem. Possibly my very first every sub 30 minute submission. Next time I'll try for sub-20!!
16. [The Floor Will Be Lava](https://adventofcode.com/2023/day/16) (2/2 stars)
    * This was slightly harder for me since I was tired and my maze traversal isn't very strong. Started off (yet again) with one-off errors in part 1 and had to implement a queue, but part 2 was ok except the running time was very very bad. I suspect this was due to the way I handled the traversal for each starting point, but honestly I'm just glad to have survived another maze puzzle.
17. [Clumsy Crucible](https://adventofcode.com/2023/day/17) (2/2 stars)
    * This was a tricky puzzle. I was trying to use DFS until I read a hint on reddit that it was more a Dijkstra problem. I will have to work on my search algorithms, but using (heavy) inspiration from u/xelt on reddit I managed to implement the algorithm using a heap-queue for speed. I don't consider this solved by me since I needed heavy help, but 2 stars is 2 stars nonetheless.
    * Also, I decided to try out the new navigation system reddit recommended in the form of dx and dy, but using a "turn-only" approach to this problem was entirely u/xelt's idea.
    * I additionally learnt my lesson from day 16 and kept track of both the direction and coordinates instead of just the latter to avoid loops and speed up the code.
18. [Lavaduct Lagoon](https://adventofcode.com/2023/day/18) (2/2 stars)
    * I initially tried to traverse and create the entire final map according to the directions, but realised it was too complicated and I kept falling short.
    * I then remembered the PTSD from day 10, so I decided to read up on the Shoelace Formula and Pick's Theorem. Turns out it was quite trivial and I could easily solve both parts after some hiccups with the hexadecimal conversions and worries about off-by-one (then I realised the question essentially mitigated all off-by-one errors, so I had nothing to worry about).
    * I essentially used the di, dj method from reddit I learnt yesterday to traverse the directions, counted edges and noted vertices, and used the Shoelace Formula to calculate internal vertices. Then, I had an off-by-two result after Pick's Theorem (internal + edges / 2 - 1) so I added 2 and got the answers for both parts. I had no idea why until...
    * [Someone on reddit](https://www.reddit.com/r/adventofcode/comments/18l0qtr/comment/kdv2206/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) said that due to external corners contributing 0.25m^2 more than normal edge pieces (which Pick's Theorem accounts for) and internal corners contributing 0.25m^2 less than normal edge pieces, the fact that there are exactly 4 more outside corners than inside corners means an additional 1m^2 has to be accounted for (which Pick's Theorem does not)
19. [Aplenty](https://adventofcode.com/2023/day/19) (2/2 stars)
    * Another blasted interval problem (PTSD from day 5 frfr). I was so stumped by part 2 that I spent 2 hours on it. Thankfully I managed to find a solution using bottom-up DP, which I'm still not very good at implementing or recognising when I need to use it.
    * I decided to use classes to represent the workflow, hoping that it would be easier. Instead I think I overdid it and spent quite a bit of time implementing it, but it was definitely fun.
20. [Pulse Propagation](https://adventofcode.com/2023/day/20) (2/2 stars)
    * Another fun exercise in classes in Python and an interesting primer to electronic circuits. I chose to manually propagate the signals, which worked better than expected and I got part 1 first try.
    * I tried to brute force part 2 but failed, then I saw a circuit diagram someone posted on the Discord, which gave me the idea to check the modules leading up to the conjunction before rx. Since the conjunction requires all inputs to itself to be high to send a low signal to rx, I checked the periods of each module and took the LCM.

# Analysis of Times and Completion
![](stats/stat_of_the_day.png?raw=true)

