# Trees

Placement-focused revision notes for Trees.

## Problems

<!-- AUTO-GENERATED START -->

### 102. Binary Tree Level Order Traversal (Medium)

🔗 LeetCode Folder: [`102-binary-tree-level-order-traversal`](../102-binary-tree-level-order-traversal)

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
    public List<List<Integer>> levelOrder(TreeNode root) {

        List<List<Integer>> result=new ArrayList<>();

        //check if root is null
        if(root ==null){
            return result;
        }
        Queue<TreeNode> queue=new LinkedList<>();
        //add root to queue
        queue.offer(root);

        while(!queue.isEmpty()){
            //get current level size
            int levelSize=queue.size();
            List<Integer> level=new ArrayList<>();

            //traverse that many nodes
            for(int i=0;i<levelSize;i++){
                TreeNode Curr = queue.poll();
                level.add(Curr.val);

                //add child node to queue
                if(Curr.left!=null){
                    queue.offer(Curr.left);
                }
                if(Curr.right!=null){
                    queue.offer(Curr.right);
                }

            }
            result.add(level);
        }
        return result;
        
    }
}
```

### 543. Diameter Of Binary Tree (Easy)

🔗 LeetCode Folder: [`543-diameter-of-binary-tree`](../543-diameter-of-binary-tree)

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
    //global variable to store value
    int diameter=0;
    public int diameterOfBinaryTree(TreeNode root) {
        //call recursive function
        findHeight(root);
        return diameter;
        
    }

    public int findHeight(TreeNode root){
        if(root==null){
            return 0;
        }

        //call recursive function
        int leftHeight=findHeight(root.left);
        int rightHeight=findHeight(root.right);

        diameter= Math.max(diameter,leftHeight + rightHeight);
        return 1 + Math.max(leftHeight, rightHeight);
    }
}
```

<!-- AUTO-GENERATED END -->
