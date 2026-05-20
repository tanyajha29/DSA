# Hashing

Placement-focused revision notes for Hashing.

## Problems

<!-- AUTO-GENERATED START -->

### 1. Two Sum (Easy)

🔗 LeetCode Folder: [`1-two-sum`](../1-two-sum)

- **Pattern:** Hashing
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

```python
class Solution:
    def twoSum(self, num, target):
        seen={}
        for i,n in enumerate(num):
            result=target-n
            if result in seen:
                return [seen[result],i]
            seen[n]=i
```

<!-- AUTO-GENERATED END -->
