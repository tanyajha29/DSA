# Two_Pointers

Placement-focused revision notes for Two_Pointers.

## Problems

<!-- AUTO-GENERATED START -->

### 15. 3sum (Medium)

🔗 LeetCode Folder: [`15-3sum`](../15-3sum)

- **Pattern:** Sorting + Two Pointers
- **Time Complexity:** O(n^2)
- **Space Complexity:** O(1)

```python
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n) :
            if i > 0 and nums[i] == nums[i - 1] :
                continue
            
            j = i + 1
            k = n - 1
            while j < k :
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum < 0 :
                    j += 1
                elif total_sum > 0 :
                    k -= 1 
                else :
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    while j < k and nums[j] == nums[j - 1] :
                        j += 1
                    
                    while j < k and nums[k] == nums[k + 1] :
                        k -= 1
        return result
```

<!-- AUTO-GENERATED END -->
