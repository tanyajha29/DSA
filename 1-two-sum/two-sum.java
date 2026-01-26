import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> seen = new HashMap<>(); // value -> index

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }

            seen.put(nums[i], i);
        }

        // If no solution found (assume one solution always exists)
        return new int[]{-1, -1};
    }

    // Optional main to test
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = sol.twoSum(nums, target);

        System.out.println("Indices: [" + result[0] + ", " + result[1] + "]");
        // Output: Indices: [0, 1]
    }
}
