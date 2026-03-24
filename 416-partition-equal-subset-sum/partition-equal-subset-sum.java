class Solution {
    public boolean canPartition(int[] nums) {
        //find sum of all nums
        int totalSum = 0;
        for (int i : nums){
            totalSum += i;
        }
        //check odd/even
        if (totalSum % 2 != 0){
            return false;
        }
        //find target 
        int target = totalSum/2;
        //use dynamic Programming
        boolean[] dp = new boolean[target + 1];
        //initialize base value
        dp[0] = true;

        for (int i : nums){
            for (int j = target; j >= i; j--){
                dp[j] = dp[j] || dp[j - i];
            }
        }
        return dp[target];
    }
}