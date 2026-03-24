# Recursion_Backtracking

Placement-focused revision notes for Recursion_Backtracking.

## Problems

<!-- AUTO-GENERATED START -->

### 416. Partition Equal Subset Sum (Medium)

🔗 LeetCode Folder: [`416-partition-equal-subset-sum`](../416-partition-equal-subset-sum)

- **Pattern:** Backtracking
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
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
```

<!-- AUTO-GENERATED END -->
