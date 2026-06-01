# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        self.total = 0
        def dfs(node) :
            if not node :
                return 0
              
            leftsum = dfs(node.left)
            rightsum = dfs(node.right)
            self.total += abs( leftsum - rightsum )
            return leftsum + rightsum + node.val

        dfs(root)
        return self.total
        
        