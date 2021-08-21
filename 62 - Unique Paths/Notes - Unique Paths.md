# Unique Paths

## Description
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

 

Example 1:
```
[R][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][*]
```
Input: m = 3, n = 7
Output: 28


Example 2:

```
[R][ ]
[ ][ ]
[ ][*]
```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:

Input: m = 7, n = 3
Output: 28

Example 4:

Input: m = 3, n = 3
Output: 6


## Notes

* Dynamic programming question that is solved with recursion + memoization
* Idea is that a `m x n` board can be broken down into smaller sized subboards
on each move down or right
  * For instance, all unique paths in `m x n` board is equal to the sum of
  unique paths in `(m-1) x n` board and unique paths in `m x (n-1)` board
    * If we move down, we get `(m-1) x n` board
    * If we move right, we get `m x (n-1)` board
* This gives us opportunity to use memoization as number of unique paths is
the same for boards of transposed sizes
  * e.g. `m x n` board has same number of unique paths as `n x m` board
  * By memoizing this, we calculate total unique paths for roughly half of the
  possible inputs/subboard sizes

* We have the following elements for recursion:
  * Base case: we are breaking the board into subboards with every move down 
  or to the right- the base case should be the smallest subboard that we can
  provide a unique path for, which is `1 x 1`. Since a `1 x 1` board is defined
  as having only one unique path, this translates to our function returning `1`
  when `m` and `n` are `1` and `1`
  * Recursive call: The total number of unique paths for a given board is 
  equal to the sum of unique paths in the subboard created by moving right and
  in the subboard created by moving down. This results in us memoizing the 
  sum of recursive calls: 
  
  ``` self.uniquePaths(m - 1, n, memo) + self.uniquePaths(m, n - 1, memo)```
  
  * Initial case: We start with the full board, so the first call to `uniquePaths` 
  takes `m` and `n` respectively

* Solution makes use of Python functions' pass by reference for arguments
  * The memo dict is created in the first/outermost call to `uniquePaths` (by
  the default argument for `memo`), and this same memo dict is passed into all
  recursive calls
  * This results in the return values of _later_ recursive calls being available
  for recursive calls that technically are deeper in the stack (despite them
  being called prior to the later ones)
* We add each calculate subboard unique path number to the memo dict before 
returning a value in each function- this ensures the intermediate results
are memoized before continuing
* Instead of using pass by reference, we can alternatively break the function 
into a non-recursive and a recursive part
  * Non-recursive part can define the memo dict and all subsequent recursive 
  calls can reference the memo dict through their outer scope

* One last thing to mention is that we return `0` anytime `m` or `n` reach a 
value of `0` themselves
  * We define a subboard with any dimension equal to `0` as having no unique paths
  * Essentially, this meant our robot moved "off" the board and hence is flagged
  as an illegal move