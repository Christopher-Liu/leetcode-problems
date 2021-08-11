# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        stack = [(root, root.val, [root.val])]
        output = []
        
        while len(stack) != 0:
            currentNode, currentSum, relPath = stack.pop()
            
            if not currentNode.right and not currentNode.left:
                if currentSum == targetSum:
                    output.append(relPath)
                
            if currentNode.right:
                stack.append((currentNode.right, currentSum + currentNode.right.val, relPath + [currentNode.right.val]))
            
            if currentNode.left:
                stack.append((currentNode.left, currentSum + currentNode.left.val, relPath + [currentNode.left.val]))
                
        return output