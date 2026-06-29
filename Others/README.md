# Others

Placement-focused revision notes for Others.

## Problems

<!-- AUTO-GENERATED START -->

### 162. Find Peak Element (Medium)

🔗 LeetCode Folder: [`162-find-peak-element`](../162-find-peak-element)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        # base case 
        # if array has a single element
        if n == 1 :
            return 0
        
        # if 1st element is the peak
        elif nums[0] > nums[1] :
            return 0

        # if last element is the peak
        elif nums[n - 1] > nums[n - 2] :
            return(n - 1)
        
        # binary search
        low = 1
        high = n - 1

        while low <= high :
            mid = (low + high) // 2 
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1] :
                return mid
            elif nums[mid] > nums[mid - 1] :
                low = mid + 1
            else :
                high = mid - 1
        return -1
```

### 907. Koko Eating Bananas (Medium)

🔗 LeetCode Folder: [`907-koko-eating-bananas`](../907-koko-eating-bananas)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # function to calculate hours
        def calculateHour( piles, speed) :
            hrs = 0
            for i in piles :
                hrs += math.ceil( i/speed )
            
            return hrs

        # binary Search
        high = max(piles)
        low = 1
        result = high
        
        while low <= high :
            mid = (low + high)//2
            total_hour = calculateHour(piles, mid)

            # check the hour value
            if total_hour <= h :
                result = mid
                high = mid - 1
            else :
                low = mid + 1
        return result
```

<!-- AUTO-GENERATED END -->
