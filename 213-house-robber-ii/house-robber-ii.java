class Solution {
    public int rob(int[] nums) {
        if(nums.length == 1){
            return nums[0];
        }

        return Math.max(
            helper(nums, 0, nums.length - 2),
            helper(nums, 1, nums.length - 1)
        );
    }

    public int helper(int [] nums, int startIndex, int EndIndex){
        int prev2 = 0;
        int prev1 = 0;

        for(int i = startIndex; i <= EndIndex; i++){
            int house = Math.max(prev1, nums[i] + prev2);
            prev2 = prev1;
            prev1 = house;
        }
        return prev1;
    }
}