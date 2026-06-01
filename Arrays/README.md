# Arrays

Placement-focused revision notes for Arrays.

## Problems

<!-- AUTO-GENERATED START -->

### 189. Rotate Array (Medium)

🔗 LeetCode Folder: [`189-rotate-array`](../189-rotate-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
'''Whole reverse:

puts desired elements in front
but reversed order

Then:

reverse front part
reverse back part

to restore order.'''
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        # rotating k times is same as k%n
        k = k % n

        # a helper function
        def helper(left, right) :
            while left < right :
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        #start rotating
        # 1. rotate whole array
        helper(0, n-1)
        # 2. rotate first k elements
        helper(0, k-1)
        # 3 rotate remaining elements
        helper(k, n-1)
```

### 561. Array Partition (Unknown)

🔗 LeetCode Folder: [`561-array-partition`](../561-array-partition)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total = 0

        for i in range(0, len(nums), 2):
            total += nums[i]
        
        return total
```

<!-- AUTO-GENERATED END -->
