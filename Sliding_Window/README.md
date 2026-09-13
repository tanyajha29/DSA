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

### 1586. Longest Subarray Of 1s After Deleting One Element (Medium)

🔗 LeetCode Folder: [`1586-longest-subarray-of-1s-after-deleting-one-element`](../1586-longest-subarray-of-1s-after-deleting-one-element)

- **Pattern:** Sliding Window
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public int longestSubarray(int[] nums) {
       int left = 0;
       int ans = 0;
       int zeros = 0;

       for (int right = 0; right < nums.length; right++){
        if (nums[right] == 0){
            zeros++;
        }
        while(zeros > 1){
            if(nums[left] == 0){
                zeros--;
            }
            left++;
        }
        ans = Math.max(ans, right - left);
       }
       return ans;
    }
}
```

<!-- AUTO-GENERATED END -->
