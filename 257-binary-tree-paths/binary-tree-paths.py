# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        result = []

        def dfs(node, path) :
            if not node :
                return

            # add the node to path
            path += str(node.val)
            if not node.left and not node.right :
                # store the current path
                result.append(path)
                return

            # recursively check the left and right node
            dfs(node.left, path+"->")
            dfs(node.right, path+"->")

        dfs(root, "")
        return result
        