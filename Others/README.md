# Others

Placement-focused revision notes for Others.

## Problems

<!-- AUTO-GENERATED START -->

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
