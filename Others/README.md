# Others

Placement-focused revision notes for Others.

## Problems

<!-- AUTO-GENERATED START -->

### 45. Jump Game Ii (Medium)

🔗 LeetCode Folder: [`45-jump-game-ii`](../45-jump-game-ii)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

_No solution file found in the LeetSync folder._

### 62. Unique Paths (Medium)

🔗 LeetCode Folder: [`62-unique-paths`](../62-unique-paths)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1] * n for _ in range(m)]

        for i in range (1, m) :
            for j in range(1, n) :
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            
        return dp[m-1][n-1]
```

### 63. Unique Paths Ii (Medium)

🔗 LeetCode Folder: [`63-unique-paths-ii`](../63-unique-paths-ii)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 :
            return 0

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for i in range(m) :
            for j in range(n) :
                if obstacleGrid[i][j] == 1 :
                    dp[i][j] = 0
                else :
                    # from top
                    if i > 0 :
                          dp[i][j] += dp[i -1][j]
                    if j > 0 :
                        dp[i][j] += dp[i][j - 1]
        
        return dp[m-1][n-1]
```

### 64. Minimum Path Sum (Medium)

🔗 LeetCode Folder: [`64-minimum-path-sum`](../64-minimum-path-sum)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        
        # fill the starting cell
        dp[0][0] = grid[0][0]
        
        # fill first row 
        for j in range(1, n) :
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # fill first column
        for i in range(1, m) :
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # fill ramaining columns
        for i in range(1, m) :
            for j in range(1, n) :
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[m-1][n-1]
```

### 67. Add Binary (Easy)

🔗 LeetCode Folder: [`67-add-binary`](../67-add-binary)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):

    def addBinary(self, a, b):

        i = len(a) - 1
        j = len(b) - 1

        carry = 0

        result = []

        while i >= 0 or j >= 0 or carry:

            total = carry

            # add from a
            if i >= 0:
                total += int(a[i])
                i -= 1

            # add from b
            if j >= 0:
                total += int(b[j])
                j -= 1

            # current binary digit
            result.append(str(total % 2))

            # update carry
            carry = total // 2

        # reverse because built backwards
        return "".join(result[::-1])
```

### 70. Climbing Stairs (Easy)

🔗 LeetCode Folder: [`70-climbing-stairs`](../70-climbing-stairs)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def climbStairs(self, n):
        if n == 1 :
            return 1
        
        if n == 2 :
            return 2
        
        first = 1
        second = 2

        for i in range (3, n + 1) :
            current = first + second
            first = second
            second = current
        
        return second
```

### 169. Majority Element (Easy)

🔗 LeetCode Folder: [`169-majority-element`](../169-majority-element)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0

        # traverse the array
        for i in nums :
            if count == 0 :
                candidate = i
            
            if i == candidate :
                count += 1
            else :
                count -= 1

        return candidate
```

### 268. Missing Number (Easy)

🔗 LeetCode Folder: [`268-missing-number`](../268-missing-number)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        exp_sum = (n*(n + 1))//2
        actual_sum = sum(nums)

        return exp_sum - actual_sum
```

### 1626. Can Make Arithmetic Progression From Sequence (Easy)

🔗 LeetCode Folder: [`1626-can-make-arithmetic-progression-from-sequence`](../1626-can-make-arithmetic-progression-from-sequence)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(2, len(arr)) :
            if arr[i] - arr[i - 1] != diff :
                return False
        
        return True
```

<!-- AUTO-GENERATED END -->
