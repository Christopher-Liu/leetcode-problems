# Target Sum

## Description
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.
 

Example 1:

    Input: nums = [1,1,1,1,1], target = 3
    Output: 5
    Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
    -1 + 1 + 1 + 1 + 1 = 3
    +1 - 1 + 1 + 1 + 1 = 3
    +1 + 1 - 1 + 1 + 1 = 3
    +1 + 1 + 1 - 1 + 1 = 3
    +1 + 1 + 1 + 1 - 1 = 3


Example 2:

    Input: nums = [1], target = 1
    Output: 1


## Notes

* We'll try to keep this from delving too deep into how to solve dynamic 
programming problems _in general_, and instead focus on how to solve this
particular problem

### General method for solving dynamic programming problems (with memoization):

1. Identify the subproblems that would solve the original problem
2. Build a brute force solution with recursion
3. Sketch a recursion tree and identify parts of the tree that represent 
redundant work being done by the algorithm
    * If we sketch out a recursion tree for a few examples, we should see that a 
    few branches repeating throughout the tree- this is indicative of redudant
    work being done & can be memoized 
4. Update brute force solution with memoization to eliminate redundant work
    * Have subproblem solutions be memoized and return memoized solutions
    * Have each recursive call check if subproblem has been solved before, so 
    the solution is in the memo, and return memoized result if so (checking and
    returning memoized solutions becomes one of the recursion base cases)


### Problem Specific Solution

* First thing to note is that we need to use _all_ integers from our input in
creating the various expressions
  * This fact guides how to build and sketch out a full recursion tree that
  results from a brute force solution



* The brute force solution would be to iterate through all possible expressions 
and count the expressions that sum to the target value
  * Since we have to use all values, we would go through all permutations of 
  `+`s and `-`s in all potential positions of the expression


