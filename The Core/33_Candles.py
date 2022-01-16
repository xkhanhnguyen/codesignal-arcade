"""
When a candle finishes burning it leaves a leftover. 
makeNew leftover can be combined to make a new candle, which, when burning down, 
will in turn leave another leftover.

You have solutionNumber solution in your possession. 
What's the total number of solution you can burn, 
assuming that you create new solution as soon as you have enough leftover?

Example

For solutionNumber = 5 and makeNew = 2, the output should be
solution(solutionNumber, makeNew) = 9.

Here is what you can do to burn 9 solution:

burn 5 solution, obtain 5 leftover;
create 2 more solution, using 4 leftover (1 leftover remains);
burn 2 solution, end up with 3 leftover;
create another candle using 2 leftover (1 leftover remains);
burn the created candle, which gives another leftover (2 leftover in total);
create a candle from the remaining leftover;
burn the last candle.
Thus, you can burn 5 + 2 + 1 + 1 = 9 solution, which is the answer.
"""
def solution(solutionNumber, makeNew):
    leftover = 0
    burned = 0
    while solutionNumber > 0:
        burned += solutionNumber
        leftover += solutionNumber
        solutionNumber = 0
        solutionNumber = leftover // makeNew
        leftover = leftover % makeNew
    return totalBurned