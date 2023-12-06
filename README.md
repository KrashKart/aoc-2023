# Overview
Hello, welcome to my AOC 2023 repo, where I post my solutions, problem data and test cases. I decided to challenge myself to complete the daily tasks to improve my coding skills and programmatic thinking.

For those unfamiliar, AOC an Advent of Code, where in the style of an advent calendar, code challenges are released everyday at 1pm Singapore Time (midnight EST or UTC-5). A problem description and problem data (in the form of text) will be given, and the solution must be entered below the problem description. There are 2 tiers of problems per day, Part 1, usually easier, and Part 2, usually a harder extension of Part 1, unlocks only after completion of Part 1. Any wrong answer will come with a 1 minute wait time (which increases after a certain amount of wrong answers) before an answer can be submitted, along with a hint whether the answer is too high or low. Completion of Part 1 only yields 1 star (silver), and that of both parts yields 2 (gold). There are no restriction on programming languages, and the time taken since opening the problem set Part 1 will be used in the global leaderboard and any private leaderboards you are registered in.

I chose to do my coding in Python 3.11. These solutions are definitely not the most efficient, but I try to make them as short and concise as possible.

Huge thanks to the creator of AOC, [Eric Wastl](http://was.tl/).

[View the AOC 2023 page here](https://adventofcode.com/2023/about)

# Days and Reflections
1. Trebuchet? (2/2 stars)
    * This was a particularly difficult day 1 from what I heard in my university discord, which I agree. I expected it to be trivial but it ended up costing me 2 hours...
2. Cube Conundrum (2/2 stars)
    * This was manageable, but my string processing was quite weak so fumbled on the regex considerably.
3. Gear Ratios (2/2 stars)
    * This was a horrible problem for me, because it seemed so tedious. I eventually opted to store each character in an n x n array, recording the indices of the groups of numbers and symbols that were not ".", and traversed the entire n x n array
4. Scratchcards (2/2 stars)
    * Very manageable actually. Solved this one quite quickly due to me being used to regex. I opted for a "bottom-up" style of dynamic programming in Part 2 which if not for a careless mistake, could've been my first sub-20 minute submission.
5. If You Give A Seed A Fertilizer (2/2 stars)
    * I must say the problem gave me quite a headache, but it did teach me the principles of logical thinking and analysis. It sounds weird, but my approach was a more mathematical and logical one as compared to my initial idea which was brute-forcing. Although the code is bulky and unoptimised, I'm quite proud of it anyway.
6. Wait For It (2/2 stars)
    * A particularly easy day, even easier than day 4. The input text was not lengthy at all, so any tricky edge cases were not included. I chose to brute force search my way through.

# Analysis of Times and Completion
![](stats/stat_of_the_day.png?raw=true)

