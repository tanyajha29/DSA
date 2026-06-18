# Arrays

Placement-focused revision notes for Arrays.

## Problems

<!-- AUTO-GENERATED START -->

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
