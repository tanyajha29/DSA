# Trees

Placement-focused revision notes for Trees.

## Problems

<!-- AUTO-GENERATED START -->

### 100. Same Tree (Easy)

🔗 LeetCode Folder: [`100-same-tree`](../100-same-tree)

- **Pattern:** Tree
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        # null case
        if not q and not p :
            return True
        
        # one null root case
        if not p or not q :
            return False
        
        #  check if root is same
        if p.val != q.val :
            return False
        
        # return by recursively checking for the left and the right sub trees
        return ( self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left))
```

### 104. Maximum Depth Of Binary Tree (Easy)

🔗 LeetCode Folder: [`104-maximum-depth-of-binary-tree`](../104-maximum-depth-of-binary-tree)

- **Pattern:** Tree
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
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
```

### 226. Invert Binary Tree (Easy)

🔗 LeetCode Folder: [`226-invert-binary-tree`](../226-invert-binary-tree)

- **Pattern:** Tree
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
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
```

### 257. Binary Tree Paths (Easy)

🔗 LeetCode Folder: [`257-binary-tree-paths`](../257-binary-tree-paths)

- **Pattern:** Tree
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
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
```

### 563. Binary Tree Tilt (Easy)

🔗 LeetCode Folder: [`563-binary-tree-tilt`](../563-binary-tree-tilt)

- **Pattern:** Tree
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
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
```

### 1484. Linked List In Binary Tree (Medium)

🔗 LeetCode Folder: [`1484-linked-list-in-binary-tree`](../1484-linked-list-in-binary-tree)

- **Pattern:** Tree
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
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
```

<!-- AUTO-GENERATED END -->
