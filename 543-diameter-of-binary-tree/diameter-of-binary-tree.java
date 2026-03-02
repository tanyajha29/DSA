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