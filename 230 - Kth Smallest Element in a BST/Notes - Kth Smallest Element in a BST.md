# Kth Smallest Element in a BST

## Description
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

```
    3
   / \
  1   4
   \
    2
```

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

```
        5
       / \
      3   6
     / \
    2   4
```
 

Constraints:

* The number of nodes in the tree is n.
* `1 <= k <= n <= 104`
* `0 <= Node.val <= 104`


## Notes

* (Binary) tree problem, so once again we consider the usual techniques of DFS
or BFS
* This problem requires us to find the `kth` smallest element in a BST, so if we 
wanted to brute force, we could simply go over all of the tree nodes
repeatedly while grabbing the _next_ lowest value each time. For complexity 
reasons, we do not want to traverse all elements multiple times
  * A good starting point for a solution would use the data structure's 
  properties that are available to us- use the BST's ordering properties

* A in-order traversal of the tree (one of the main ways to do DFS) would result
in us visiting each node in ascending order 
  * Recall in-order traversal is left-visit-right
* Following the trend of tree problem solutions usually being DFS of BFS with 
some adjustments to return the desired value, we make the adjustments in
the visit step of the traversal

* For my solution, I opted to do a full in-order traversal of the tree with 
recursion
  * The recursion is adjusted to allow for data to be passed up and down 
  the call stack by return statements and the `kthVal` parameter respectively-
  allowing for values to be passed _up_ the call stack is necessary for 
  returning the `kth` lowest value once we've found it
* From in-order traversal properties, we know that the first node visit step is \the lowest value, followed by the second lowest, third lowest, and so forth
  * The solution uses a counter (`nodesVisited`) to keep track of how many
  nodes visited. Once we have visited the `kth` node, we know that this must be
  the `kth` lowest value that we are seeking 
    * The counter is passed up and down the call stack and incremented at each
    visit step. We also pass along along with the `kth` lowest value once we've 
    found it
* Note that we split the solution into a non-recursive part and a recursive part

* In order to avoid traversing the entire tree when not needed, we have the
base case that immediately returns `nodesVisited` and `kthVal` when we've 
already found our desired solution
  * In the case that `k` is significantly smaller than the total number of 
  nodes in the tree, having to traverse the entire tree _anyways_ results in us
  needlessly traverse many nodes when we've already gotten the answer
  * Without this terminating base case, we would still have a working solution,
  just one that is _relatively naive_ and does a full tree traversal each time
  