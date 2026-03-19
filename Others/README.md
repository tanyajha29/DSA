# Others

Placement-focused revision notes for Others.

## Problems

<!-- AUTO-GENERATED START -->

### 112. Path Sum (Easy)

🔗 LeetCode Folder: [`112-path-sum`](../112-path-sum)

- **Pattern:** General
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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        //check if null
        if(root == null){
            return false;
        }

        //if we reach leaf node
        if(root.left == null && root.right == null){
            //check if remSum = targetsum
            return targetSum == root.val;
        }

        //subtrack current node from targetsum
        int remSum = targetSum - root.val;
        //move to left or right child
        return hasPathSum(root.left , remSum) || hasPathSum(root.right, remSum); 
    }
}
```

### 125. Valid Palindrome (Easy)

🔗 LeetCode Folder: [`125-valid-palindrome`](../125-valid-palindrome)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public boolean isPalindrome(String s) {
        //two pointers
        int left = 0; //start
        int right = s.length() -1; //end

        while(left < right)
        {
             //skip non alphanumeric character
             while(left < right && !Character.isLetterOrDigit(s.charAt(left))){
                left++;
             }
             while(left < right && !Character.isLetterOrDigit(s.charAt(right))){
                right--;
             }
             //move pointers on match else return false
             if(Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))){
                return false;
             }
             left++;
             right--;
        }
        return true;
    }
}
```

<!-- AUTO-GENERATED END -->
