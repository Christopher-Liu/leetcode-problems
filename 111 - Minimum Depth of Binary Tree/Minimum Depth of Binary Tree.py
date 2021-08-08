# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            # edge case of empty tree being passed in
            return 0
        elif not root.left and not root.right:
            # we hit a leaf- stop recursive calls
            return 1
        elif not root.left and root.right:
            return self.minDepth(root.right) + 1
        elif not root.right and root.left:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


        # Condensed solution that only needs 3 conditionals:
        # if not root:
        #     return 0
        # elif not root.left or not root.right:
        #     return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # else:
        #     return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        