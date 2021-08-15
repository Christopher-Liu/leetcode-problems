# Path Sum III

## Description
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8

```
         10
        /  \
       5    -3
      / \     \
     3   2     11
    / \   \     
   3  -2   1     

```

Output: 3

Explanation: You have the paths of `[5, 3]` and `[5, 2, 1]` from the left
subtree, and `[-3, 11]` from the right subtree that each add up to 8.


Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3


## Notes

* Another tree problem, so we consider DFS and BFS as our main algorithms
* Since we want to look at downward-spanning paths, DFS is the algorithm that
most naturally lets us search the tree in a suitable way

* This problem utilizes the same type of solution as Path Sum I and Path Sum II
* We still do a stack-based DFS, and consider what extra data we can store in
our stack elements that will be useful for this problem
* Since we want to perform a node-to-root path sum check for each node we 
land on, storing upward paths from each node to the root would be useful data
to store
  * This part is arguably space inefficient, as each of the list elements store
  quite redundant information in the paths
  * This inefficiency can be alleviated if our data structure contained parent 
  pointers which allowed us to easily traverse upwards without storing extra 
  data- _good to consider if asked about how to improve the solution_ 

* At each node, we can simply iterate through the relative path from that node
up to the root (using the extra array we are storing) and sum up the path sum
along the way
  * If we reach the target sum, we can append some sort of counter by 1
  * After we've traversed the tree, we simply return the counter
* This may be a half-baked thought, but is it possible to improve the efficiency
of this step? Maybe we can do something resembling memoization that would allow
us to skip over some of the calculations- need to consider this further

**Note**: the above is essentially a brute force algorithm