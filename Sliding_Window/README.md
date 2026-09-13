# Sliding_Window

Placement-focused revision notes for Sliding_Window.

## Problems

<!-- AUTO-GENERATED START -->

### 643. Maximum Average Subarray I (Easy)

🔗 LeetCode Folder: [`643-maximum-average-subarray-i`](../643-maximum-average-subarray-i)

- **Pattern:** Sliding Window
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sum = 0;

        // first window
        for(int i = 0; i < k; i++){
            sum += nums[i];
        }
        int maxSum = sum;
        // sliding window 
        for (int right = k; right < nums.length; right++){
            sum += nums[right];
            sum -= nums[right - k];

            maxSum = Math.max(maxSum, sum);
        }

        return (double) maxSum/k;
    }
}
```

<!-- AUTO-GENERATED END -->
