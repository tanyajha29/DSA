# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        def dfs(listnode, treenode) :

            # complete listnode matched
            if not listnode :
                return True
            
            # Tree ended
            if not treenode :
                return False
            
            # value mismatched
            if listnode.val != treenode.val :
                return False

            # mode listnode forward and treenode left or right
            # recursively check each node
            return( dfs(listnode.next, treenode.right)
            or
            dfs(listnode.next, treenode.left))

        # last node reached/ root ended
        if not root :
            return False

        # start checking here or move forward
        return( dfs(head,root)
        or
        self.isSubPath(head, root.left)
        or
        self.isSubPath(head, root.right) )
         