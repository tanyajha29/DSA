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

### 567. Permutation In String (Medium)

🔗 LeetCode Folder: [`567-permutation-in-string`](../567-permutation-in-string)

- **Pattern:** Backtracking
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_len = Counter()
        # points to start of window
        left = 0

        for right in range (len(s2)):
            # add element in the window
            window_len[s2[right]] += 1

            # check window size 
            if right - left + 1 > len(s1):
                window_len[s2[left]] -= 1

                # delete the less frequency element
                if window_len[s2[left]] == 0:
                    del window_len[s2[left]]
                left += 1

            if window_len == s1_count:
                return True
        return False
```

<!-- AUTO-GENERATED END -->
