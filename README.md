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
1. Trebuchet? (2/2 stars)
    * This was a particularly difficult day 1 from what I heard in my university discord, which I agree. I expected it to be trivial but it ended up costing me 2 hours...
2. Cube Conundrum (2/2 stars)
    * This was manageable, but my string processing was quite weak so fumbled on the regex considerably.
3. Gear Ratios (2/2 stars)
    * This problem seemed tedious at first. I eventually opted to store each character in an n x n array, recording the indices of the groups of numbers and symbols that were not ".", and traversed the entire n x n array
4. Scratchcards (2/2 stars)
    * Very manageable actually. Solved this one quite quickly due to me being used to regex. I opted for a "bottom-up" style of dynamic programming in Part 2 which if not for a careless mistake, could've been my first sub-20 minute submission.
5. If You Give A Seed A Fertilizer (2/2 stars)
    * This was slightly complicated to wrap my head around. My approach was a more mathematical and logical one in part 2 as compared to my initial idea which was brute-forcing.
6. Wait For It (2/2 stars)
    * A particularly easy day, even easier than day 4. The input text was not lengthy at all, so any tricky edge cases were not included. I chose to brute force search my way through.
7. Camel Cards (2/2 stars)
    * A fantastic problem of ranking poker combinations. I did not use regex and instead opted for the Collections module as suggested in my university Discord. I must disclose that I knew about the problem before I opened it (but after the leaderboard was already filled) thus my completion times were quite sus.
8. Haunted Wasteland (2/2 stars)
    * I was undaunted initially because I had solved several node-pathfinding problems on LeetCode before, thus part 1 didn't require too much thinking. For part 2, I messed up my order of execution of functions, and coupled with my initial idea to brute force (which failed due to the large magnitude of the answer), this caused a delay in solving part 2. I managed to figure out an alternative, faster solution in the form of the lcm function in the math module.
9. Mirage Maintenance (2/2 stars)
    * Quite an easy series puzzle. I started on this on day 10 as I was busy but completed it in less than 45 minutes
10. Pipe Maze (2/2 stars technically)
    * Part 1 was alright, I made a few logical errors which significantly delayed my score but I was able to solve it using a simple traversal. Part 2 on the other hand was simply too difficult. I had the right idea of counting the parity of the turns and straights to the left of any non-loop elements, but somehow my answer was off by 10. I resorted to searching for solutions in the reddit, so technically I have the 2nd star although I did not finish part 2.
    * Also my mathematical thinking and graph theory were too weak, so I did not consider Hamiltonian circuits or some other theorem that I don't know of.
11. Cosmic Expansion (2/2 stars)
    * I misread the question so I thought it was harder than it really was, but it was a relatively simple problem which I managed to figure out quickly once I ironed out implementation mistakes. I've been starting to think more mathematically rather than brute-forcing-ly so I guess that is good too.
    * Also, AOC has been training me to use itertools and other libraries in Python more often, which I really appreciate.
12. Hot Springs (2/2 stars)
    * An interesting Dynamic Programming problem. This introduced me to the @cache decorator in functools and how to memoize in Python. I only understood how to do this after reading a hint on the reddit, but nonetheless quite proud of my solution (although it could be better)
13. Point of Incidence (2/2 stars)
    * I was stuck initially because I tried to use maths to figure out the middle, but I realised that I could just try every line between each row to see which one the middle was.
    * Part 2 was simply to refactor my check_height() function to account for smidges, which did not take long.

# Analysis of Times and Completion
From Day 9 onwards, all timings are recorded from when I opened the problem set, not when the problem set is released. I will still indicate if I start late or did not finish as per normal

![](stats/stat_of_the_day.png?raw=true)

