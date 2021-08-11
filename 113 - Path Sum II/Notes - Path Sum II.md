# Path Sum II

## Description
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22

```
          5
         / \
        4   8
       /   / \
      11  13  4
     / \       \
    7   2       1
```

Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:

Input: root = [1,2,3], targetSum = 5

```
    1
   / \
  2   3
```

Output: []

Example 3:

Input: root = [1,2], targetSum = 0

```
   1
    \
     2
```

Output: []


## Notes

* Very similar to problem 112 Path Sum. This problem is more or less an 
extension of that problem to have one additional dimension of values to consider
* Refer to notes for 112 Path Sum for most of the explanations on how the code
works and why certain things were implemented

* As with everything else, we have a tree problem so we do want to consider
DFS or BFS as our main algorithms
* Main difference with this problem is that we still want to keep track of the
relative path sums, but this time return the paths that provide a path sum
equal to the target sum (not just a boolean value)
* Continuing with the theme of augmenting our data structures to store 
additional data that we would need to reference, we can very intuitively 
extend our stack tuples to include the relative paths as a third element
  * By storing the relative paths from root to the current node along with the
  node itself and the relative path sum, we have easy access to the paths as
  soon as we find a matching path sum

* Since the answer wants a list of all paths that provide the desired path sum,
we can start with an empty output list and iteratively append any future paths
into this list if they satisfy our path list requirement

* Once again, this solution is just stack-based DFS with minor tweaks 
  * The tweaks being that the stack holds tuples instead of just the nodes, and
  the tuples hold additional data that we need to keep track of
