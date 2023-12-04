# Overview
Hello, welcome to my AOC 2023 repo, where I post my solutions, problem data and test cases. I decided to challenge myself to complete the daily tasks to improve my coding skills and programmatic thinking.

For those unfamiliar, AOC an Advent of Code, where in the style of an advent calendar, code challenges are released everyday at 1pm Singapore Time (midnight EST or UTC-5). A problem description and problem data (in the form of text) will be given, and the solution must be entered below the problem description. There are 2 tiers of problems per day, Part 1, usually easier, and Part 2, usually a harder extension of Part 1, unlocks only after completion of Part 1. Any wrong answer will come with a 1 minute wait time (which increases after a certain amount of wrong answers) before an answer can be submitted, along with a hint whether the answer is too high or low. There are no restriction on programming languages, and the time taken since opening the problem set Part 1 will be used in the global leaderboard and any private leaderboards you are registered in.

I chose to do my coding in Python 3.11. These solutions are definitely not the most efficient, but I try to make them as short and concise as possible.

Huge thanks to the creator of AOC annually, [Eric Wastl](http://was.tl/)

[View the AOC 2023 page here](https://adventofcode.com/2023/about)

# Days, Descriptions and Comments
1. Trebuchet? (<span style="color:Gold">2/2</span> stars)
    * Part 1: Given a chunk of alphanumeric text, add up the first and last digits spelt out (1 = "one", etc) that appear in each line for all lines
    * Part 2: Now re-do Part 1 but include any actual numerics as well (1 could be "1" or "one", etc)
    * This was a particularly difficult day 1 from what I heard in my university discord, which I agree. I expected it to be trivial but it ended up costing me 2 hours...
2. Cube Conundrum (<span style="color:gold">2/2</span> stars)
    * Part 1: Given a chunk of games (1 game per line) and their IDs involving the amount of red, green and blue balls drawn over multiple turns, figure out the sum of the possible game IDs given limited balls.
    * Part 2: Given the same text, figure out the product of the minimum numbers of red, blue and green balls needed for each game to be possible per line (the power set of the number of balls)
    * This was manageable, but my string processing was quite weak so fumbled on the regex
3. Gear Ratios
    * Part 1: Given a chunk of numbers and symbols separated by one or more "."s, find the sum of the numbers adjacent to any symbol that is not a "."
    * Part 2: Using the same text, find the sum of the product of two numbers adjacent to those gears. The gears must be adjacent to 2 and only 2 gears to be included in the sum.
    * This was a horrible problem for me, because it seemed so tedious. I eventually opted to store each character in an n x n array, recording the indices of the groups of numbers and symbols that were not ".", and traversed the entire n x n array
4. Scratchcards
    * Part 1: Given scratchcards with winning numbers and numbers you have (both unique for each card), find the number of points total given n matching numbers yields 2 ^ n points unless there is no match, which yields 0 points
    * Part 2: Given the same text, find the total number of scratchcards you have in the end given n matching numbers on scratchcard q rewards you with copies of scratchcards q + 1, ..., q + n if n is not 0
    * Very manageable actually. Solved this one quite quickly due to me being used to regex. I opted for a "bottom-up" style of dynamic programming in Part 2


# Analysis of Times and Completion
![](stats/stat_of_the_day.png?raw=true)

