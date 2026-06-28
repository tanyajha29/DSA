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

### 152. Maximum Product Subarray (Medium)

🔗 LeetCode Folder: [`152-maximum-product-subarray`](../152-maximum-product-subarray)

- **Pattern:** Sliding Window
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def maxProduct(self, nums):
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in nums[1:] :
            if i < 0 :
                # why swap
                '''multiplying by -ve number flips sign'''
                max_product, min_product = min_product, max_product
            
            max_product = max(i, max_product * i)
            min_product = min(i, min_product * i)
            result = max(result, max_product)

        return result
```

### 209. Minimum Size Subarray Sum (Medium)

🔗 LeetCode Folder: [`209-minimum-size-subarray-sum`](../209-minimum-size-subarray-sum)

- **Pattern:** Sliding Window
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):

    def minSubArrayLen(self, target, nums):

        left = 0
        curr_sum = 0

        min_len = float('inf')

        for right in range(len(nums)):

            # add current element
            curr_sum += nums[right]

            # shrink window
            while curr_sum >= target:

                min_len = min(right - left + 1, min_len)

                curr_sum -= nums[left]

                left += 1

        if min_len == float('inf'):
            return 0

        return min_len
```

### 2868. Continuous Subarrays (Medium)

🔗 LeetCode Folder: [`2868-continuous-subarrays`](../2868-continuous-subarrays)

- **Pattern:** Sliding Window
- **Time Complexity:** TBD
- **Space Complexity:** TBD

_No solution file found in the LeetSync folder._

<!-- AUTO-GENERATED END -->
