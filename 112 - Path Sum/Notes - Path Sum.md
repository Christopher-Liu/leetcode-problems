# Path Sum

## Description

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22

```
          5
         / \
        4   8
       /   / \
      11  13  4
     / \       \
    7   2       1
```

Output: true

Example 2:

Input: root = [1,2,3], targetSum = 5

```
    1
   / \
  2   3
```

Output: false

Example 3:

Input: root = [1,2], targetSum = 0

```
   1
    \
     2
```

Output: false


## Notes

* Another binary tree problem that requires us to traverse through the nodes, 
so we consider DFS and BFS
  * Summing up the node values on paths from root to leaves inherently requires
  us to traverse _downwards_, so DFS is a natural method to use
  * Since we want the sums of values for each path, we could consider doing DFS
  while keeping track of the path sums with some sorts of counters

* The solution I went with (based off others I saw on leetcode's discussions)
relied on a stack to do DFS instead of the usual recursion. I saw this as good
practice with implementing DFS in a different way
  * The solution is a straight forward implementation of DFS with additional 
  variables used to keep track of relative path sums from the root up until each
  of the nodes that we visit
  * We perform a DFS and keep track of path sums. Once we hit a leaf node 
  (denoted by conditional that checks if no left or right child exists), we 
  just need to compare the path sum to our target sum and return `True` if so
  * We let this run until the stack is empty, which is when we've finished our
  traversal and arrive back at the root, and return `False` (since we've 
  finished traversing the whole tree and did _not_ get a path sum equal to the
  target sum at any point)

* An interesting technique used in this solution is to not just store the nodes
in the stack, but to store tuples that contain extra data
  * The tuples we store include the nodes that we are traversing, as well as
  the path sums from the root _up until that node itself_
  * These relative path sums allow us to track what the sums are up until that
  point of traversing, which is useful when the nodes have left and right 
  children and we need to separately calculate the branching path sums- storing
  the relative path sums makes this very easy to do

* So all in all, it will be a good remember this technique of storing extra bits 
of data in our implementation that helps keep track of program state
  * The "normal" implementation of DFS would store just the nodes in the stack-
  by storing tuples with relative path sums, calculating the path sums to the 
  leaves is as simple as grabbing the relative path sum that is attached to the
  leaf node itself
  * Always consider how we can make small adjustments to the data structures
  and algorithms to suit the problem's needs
