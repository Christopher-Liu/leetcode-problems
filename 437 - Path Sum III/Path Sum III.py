# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        equalPaths = 0
        stack = [(root, [root.val])]
        
        while len(stack) != 0:
            currentNode, pathFromRoot = stack.pop()
            
            relativeSum = 0
            
            for nodeVal in reversed(pathFromRoot):
            
                relativeSum += nodeVal
                
                if relativeSum == targetSum:
                    equalPaths += 1
                
            if currentNode.right:
                stack.append((currentNode.right, pathFromRoot + [currentNode.right.val]))
            
            if currentNode.left:
                stack.append((currentNode.left, pathFromRoot + [currentNode.left.val]))
                
        return equalPaths