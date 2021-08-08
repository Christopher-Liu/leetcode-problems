# Minimum Depth of Binary Tree

## Description

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

Input: root = [3,9,20,null,null,15,7]
```
     3
    / \
   9  20
      / \
     15  7
```
Output: 2


Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]  

```
    2
     \
      3
       \
        4
         \
          5
           \
            6
```
Note that leetcode gives inconsistent formatting of the input list/array- the
above is to be read like a long chain of nodes with only right childs and NOT
in levelwise order (which is how the first example's array is to be read)


Output: 5


## Notes

* Problem is very similar to finding max depth of a binary tree, except
adjustments need to be made to find minimum depth instead
  * So we still need to traverse from the root to the leaves of the tree, but
  make sure to keep track of paths that are _shortest_ (smallest value for 
  heights) 
* 