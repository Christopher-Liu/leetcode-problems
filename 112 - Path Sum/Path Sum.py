# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
    
        # We'll implement DFS with a stack this time around.

        # Useful trick is to store tuples instead of individual objects in 
        # stack/list. The tuple in this case contains extra data for keeping 
        # track of program state at various instances that will make it easier
        # to add up the path sum. 
        stack = [(root, root.val)]
        
        # Stack-based DFS runs until our stack is empty
        while len(stack) != 0:
            currentNode, currentSum = stack.pop()
            
            if not currentNode.right and not currentNode.left:
                if currentSum == targetSum:
                    return True
            
            # Note to get the correct DFS order, we must push the right child
            # before the left child node each time. Since we are popping in each 
            # iteration, this insures that we always traverse left before 
            # traversing right (because the left child is always pushed last,
            # meaning it gets popped first).
            if currentNode.right:
                stack.append((currentNode.right, currentSum + currentNode.right.val))
            
            if currentNode.left:
                stack.append((currentNode.left, currentSum + currentNode.left.val))
                             
        return False