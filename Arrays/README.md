# Arrays

Placement-focused revision notes for Arrays.

## Problems

<!-- AUTO-GENERATED START -->

### 26. Remove Duplicates From Sorted Array (Easy)

🔗 LeetCode Folder: [`26-remove-duplicates-from-sorted-array`](../26-remove-duplicates-from-sorted-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

_No solution file found in the LeetSync folder._

### 33. Search In Rotated Sorted Array (Medium)

🔗 LeetCode Folder: [`33-search-in-rotated-sorted-array`](../33-search-in-rotated-sorted-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            # target found
            if nums[mid] == target:
                return mid

            # LEFT HALF SORTED
            if nums[left] <= nums[mid]:

                # target inside left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # RIGHT HALF SORTED
            else:

                # target inside right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
```

### 34. Find First And Last Position Of Element In Sorted Array (Medium)

🔗 LeetCode Folder: [`34-find-first-and-last-position-of-element-in-sorted-array`](../34-find-first-and-last-position-of-element-in-sorted-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)
        def firstOccurence(nums, n, target) :
            first = -1
            low = 0
            high = n - 1
            
            while low <= high :
                mid = (low + high)//2
                if nums[mid] == target :
                    first = mid
                    high = mid - 1
                elif nums[mid] < target :
                    low = mid + 1
                else :
                    high = mid -1
            
            return first

        def lastOccurence(nums, n, target) :
            last = -1
            low = 0
            high = n - 1
            
            while low <= high :
                mid = (low + high)//2
                if nums[mid] == target :
                    last = mid
                    low = mid + 1
                elif nums[mid] < target :
                    low = mid + 1
                else :
                    high = mid -1
            
            return last

        first = firstOccurence(nums, n, target)
        if first == -1 :
            return [-1, -1]
        
        last = lastOccurence(nums, n, target)
        return [first, last]
```

### 48. Rotate Image (Medium)

🔗 LeetCode Folder: [`48-rotate-image`](../48-rotate-image)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n) :
            for j in range(i + 1, n) :
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for rows in matrix :
            rows.reverse()
```

### 54. Spiral Matrix (Medium)

🔗 LeetCode Folder: [`54-spiral-matrix`](../54-spiral-matrix)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution:
    def spiralOrder(self, matrix):
        left = 0
        top = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        # array to store the result
        result = []
        while top <= bottom and left <= right :
            # traverse from left to right
            for i in range(left, right + 1) :
                result.append(matrix[top][i])
            top += 1

            # traverse from top to bottom
            for j in range(top, bottom + 1) :
                
                # store
                result.append(matrix[j][right])
            right -= 1
            
            # traverse from right to left
            if top <= bottom :
                for i in range(right, left - 1, -1) :
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            #  traverse from bottom to top
            if left <= right :
                for i in range(bottom, top - 1, -1) :
                    result.append(matrix[i][left])
                left += 1

        return result
```

### 73. Set Matrix Zeroes (Medium)

🔗 LeetCode Folder: [`73-set-matrix-zeroes`](../73-set-matrix-zeroes)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

_No solution file found in the LeetSync folder._

### 81. Search In Rotated Sorted Array Ii (Medium)

🔗 LeetCode Folder: [`81-search-in-rotated-sorted-array-ii`](../81-search-in-rotated-sorted-array-ii)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high :
            mid = (low + high)//2

            if nums[mid] == target :
                return True
            
            # case in which array is not sorted 
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1 
                high -= 1
                continue
            
            # left half is sorted
            if nums[low] <= nums[mid] :
                if nums[low] <=target <= nums[mid] :
                    high = mid - 1
                else :
                    low = mid + 1
            # right half is sorted
            else :
                if nums[mid] <=target <= nums[high] :
                    low = mid + 1
                else :
                    high = mid - 1
        return False
```

### 88. Merge Sorted Array (Easy)

🔗 LeetCode Folder: [`88-merge-sorted-array`](../88-merge-sorted-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1; //valid last element of num1
        int j = n - 1; //last element of nums2
        int k = m + n -1; //last element of num1

        //itetrate till one array has no element to itetrate
        while (i >= 0 && j >= 0){
            if (nums1[i] > nums2[j]){
                nums1[k] = nums1[i];
                i--;
            }else{
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        } 
        //if nums2 still hast elements left
        while(j >= 0){
            nums1[k] = nums2[j];
            j--;
            k--;
        }
    }
}
```

### 121. Best Time To Buy And Sell Stock (Easy)

🔗 LeetCode Folder: [`121-best-time-to-buy-and-sell-stock`](../121-best-time-to-buy-and-sell-stock)

- **Pattern:** Greedy / One Pass
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

```python
class Solution(object):
    def maxProfit(self, prices):
        #declare and initialize variables
        min_pr=float('inf')
        max_pr=0

        #loop through all values/price
        for price in prices:
            # check and initalize min price
            if price < min_pr:
                min_pr = price
            #check profit and buy time
            profit = price - min_pr

            # check and initalize max price
            if profit > max_pr:
                max_pr = profit
        return max_pr
```

### 153. Find Minimum In Rotated Sorted Array (Medium)

🔗 LeetCode Folder: [`153-find-minimum-in-rotated-sorted-array`](../153-find-minimum-in-rotated-sorted-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1
        result = nums[0]

        while low <= high :
            mid = (low + high) // 2
            # if left half is sorted
            if nums[low] <= nums[mid] :
                result = min(result, nums[low])
                low = mid + 1
            # if right half is sorted
            else:
                high = mid -  1
                result = min(result, nums[mid])

        return result
```

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

### 215. Kth Largest Element In An Array (Medium)

🔗 LeetCode Folder: [`215-kth-largest-element-in-an-array`](../215-kth-largest-element-in-an-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort(reverse = True)
        return nums[k-1]
```

### 525. Contiguous Array (Medium)

🔗 LeetCode Folder: [`525-contiguous-array`](../525-contiguous-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def findMaxLength(self, nums):
        # avariable with structure {prefix_sum : index}
        hashmap = {0 : -1}
        prefix_sum = 0
        max_len = 0
        for i in range( len(nums) ) :
            if nums [i] == 0 :
                prefix_sum -= 1
            else :
                prefix_sum += 1
            
            if prefix_sum in hashmap :
                length = i - hashmap[prefix_sum]
                max_len = max(length, max_len)
            else :
                hashmap[prefix_sum] = i
            
        return max_len
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

### 565. Array Nesting (Medium)

🔗 LeetCode Folder: [`565-array-nesting`](../565-array-nesting)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def arrayNesting(self, nums):
        # to track processed elements.
        visited = set()
        max_len = 0

        '''Loop through every index.
        If already visited: skip.'''

        for i in range( len(nums) ) :
            if i in visited :
                continue
            
            #start traversal from current index.
            count = 0
            current = i

            '''While current not visited:mark visited
            move to next index
            increase count'''

            while current not in visited :
                visited.add(current)

                #jump to next index
                current = nums[current]
                count += 1 

            #Update maximum length.
            max_len = max(count, max_len)
        return max_len
```

### 978. Valid Mountain Array (Easy)

🔗 LeetCode Folder: [`978-valid-mountain-array`](../978-valid-mountain-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i = 0
        n = len(arr)
        
        # increasing order till peak
        while i < n - 1 and arr[i] < arr[i + 1] :
            i += 1
        
        # peak cannot be at start or end
        if i == 0 or i == n - 1 :
            return False

        # decreasing order after peak
        while i < n - 1 and arr[i] > arr[i + 1] :
            i += 1

        # must reach end
        return i == n - 1
```

### 2271. Rearrange Array Elements By Sign (Medium)

🔗 LeetCode Folder: [`2271-rearrange-array-elements-by-sign`](../2271-rearrange-array-elements-by-sign)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def rearrangeArray(self, nums):
        negIndex = 1
        posIndex = 0
        n = len(nums)
        result = [0] * n

        for i in range (n) :
            if nums[i] < 0 :
                result[negIndex] = nums[i]
                negIndex += 2
            else :
                result[posIndex] = nums[i]
                posIndex += 2
        return result
```

<!-- AUTO-GENERATED END -->
