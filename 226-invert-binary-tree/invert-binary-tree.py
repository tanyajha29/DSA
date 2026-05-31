# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root :
            return None

        # swap the left and right nodes
        root.left, root.right = (
            root.right,
            root.left
        )

        # recursively do the same for the right and left nodes 
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
        