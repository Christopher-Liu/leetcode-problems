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

* Given that this is a (binary) tree problem, we consider the usual tree 
patterns of doing some DFS, BFS, or variant of them

* Problem is very similar to finding max depth of a binary tree, except
adjustments need to be made to find minimum depth instead
  * Immediately, we should think of finding the `min` of the left and right 
  subtree heights instead of max. This turns out to be the bulk of the solution

* Need to traverse from the root to the leaves and keep track of paths that 
are _shortest_ (so we are interested in smaller heights this time) 
  * Recursive DFS should to mind as the way to traverse down to leaves
  * Need to consider what cases we will encounter on while traversing and what
  to do at each traversal step to properly calculate the min depth

* We can identify three main cases while traversing:
  1. Encounter a leaf (node with no children): this should be the base case
  in our recursion- when we hit a node, we stop recursively traversing and 
  return a height value of 0
  2. Encounter a node with both children: we we grab the minimum depth between
  the left and right subtrees _plus 1_. The addition of 1 is how the algorithm
  counts each level
  3. Encounter a node with one child node: this case requires more discussion,
  provided below

* One caveat is that minimum depth is defined as the number of nodes from the 
root to the nearest leaf (nearest node with no child nodes)
  * We cannot simply recursively take the `min` of the left and right subtree 
  heights (and add 1) for all nodes and get the right answer
    * If a node has only one child node, then non-existing child node would
    be a subtree of height 0 and always be the minimum of the two subtrees (0
    is less than any other positive value)
    * Need to take this into account and have the solution consider depths only
    from from existing subtrees
* The simplest solution when we encounter a node with one child node, we 
continue traversing only in the direction with an existing child
  * This can be done by adding two `elif` conditions for each child node 
  separately existing and traversing in the direction that exists
    * This can be done in one step, however, by grabbing the maximum of the 
    two subtrees- this is done in the condensed solution
    * The non-existent subtree should return height 0, so the `max` call results 
    in always grabbing the height of the existing subtree

* The rest of the cases are represented in a straightforward fashion in the
if-else block of the solution