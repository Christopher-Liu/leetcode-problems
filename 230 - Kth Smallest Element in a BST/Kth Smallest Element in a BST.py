# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodesVisited = 0
        kthVal = None
        
        results = self.kthSmallestRecurse(root, k, nodesVisited, kthVal)
        
        return results[1]
    

    # Recursive portion of function- does inorder traversal of BST
    def kthSmallestRecurse(self, root: Optional[TreeNode], k: int, nodesVisited: int, kthVal: int) -> int:
        # If we've already found the kth lowest value, we can stop the 
        # traversal and pass the solution up the call stack
        if (nodesVisited == k):
            return (nodesVisited, kthVal)

        if root.left:
            (nodesVisited, kthVal) = self.kthSmallestRecurse(root.left, k, nodesVisited, kthVal)
        
        nodesVisited += 1
        if (nodesVisited == k):
            kthVal = root.val
        
        if root.right:
            (nodesVisited, kthVal) = self.kthSmallestRecurse(root.right, k, nodesVisited, kthVal)
            
        return (nodesVisited, kthVal)
        