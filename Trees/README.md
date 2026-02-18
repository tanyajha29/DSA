# Trees

Placement-focused revision notes for Trees.

## Problems

<!-- AUTO-GENERATED START -->

### 199. Binary Tree Right Side View (Medium)

🔗 LeetCode Folder: [`199-binary-tree-right-side-view`](../199-binary-tree-right-side-view)

- **Pattern:** Tree
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result=new ArrayList<>();

        dfs_right_searcha(root, 0, result);
        return result;
        
    }

   public void dfs_right_searcha(TreeNode node, int level, List<Integer>result){
        if(node==null) return;

        if(level==result.size()){
            result.add(node.val);
        }
            dfs_right_searcha(node.right, level+1, result);
            dfs_right_searcha(node.left, level+1, result);
        
    }
}
```

<!-- AUTO-GENERATED END -->
