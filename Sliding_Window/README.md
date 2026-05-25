# Sliding_Window

Placement-focused revision notes for Sliding_Window.

## Problems

<!-- AUTO-GENERATED START -->

### 3. Longest Substring Without Repeating Characters (Medium)

🔗 LeetCode Folder: [`3-longest-substring-without-repeating-characters`](../3-longest-substring-without-repeating-characters)

- **Pattern:** Sliding Window
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_len = 0
        seen = set()

        for right in range (len(s)):
            # check duplicates
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max( max_len, right - left +1)
        return max_len
```

### 53. Maximum Subarray (Medium)

🔗 LeetCode Folder: [`53-maximum-subarray`](../53-maximum-subarray)

- **Pattern:** Sliding Window
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range (1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(curr_sum,  max_sum)
        return max_sum
```

<!-- AUTO-GENERATED END -->
