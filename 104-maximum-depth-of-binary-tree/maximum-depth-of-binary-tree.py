# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #base case
        if not root :
            return 0
        
        # check left and right subtree recursively
        rightDepth = self.maxDepth(root.right)
        leftDepth = self.maxDepth(root.left)
        
        return ( max(rightDepth, leftDepth) + 1 )