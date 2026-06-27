# Sliding_Window

Placement-focused revision notes for Sliding_Window.

## Problems

<!-- AUTO-GENERATED START -->

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

### 2868. Continuous Subarrays (Medium)

🔗 LeetCode Folder: [`2868-continuous-subarrays`](../2868-continuous-subarrays)

- **Pattern:** Sliding Window
- **Time Complexity:** TBD
- **Space Complexity:** TBD

_No solution file found in the LeetSync folder._

<!-- AUTO-GENERATED END -->
