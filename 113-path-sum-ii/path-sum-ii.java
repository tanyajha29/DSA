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
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result=new ArrayList<>();

        find_targetSum(root, targetSum, new ArrayList<>(), result);
        return result;
    }

    //recursive function
    public void find_targetSum(TreeNode node, int target, List<Integer> current,  List<List<Integer>> result){
        if(node==null){
            return;
        }

        //add value to the list
        current.add(node.val);

        //check leafnode 
        if(node.right==null && node.left==null && target==node.val){
            result.add(new ArrayList<>(current));
        }

        //recurse left and right
        find_targetSum(node.left, target-node.val, current, result);
        find_targetSum(node.right, target-node.val, current, result);

        //backtracking
        current.remove(current.size()-1);
    }
}