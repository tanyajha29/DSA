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

### 49. Group Anagrams (Medium)

🔗 LeetCode Folder: [`49-group-anagrams`](../49-group-anagrams)

- **Pattern:** Sorting / Hashing
- **Time Complexity:** O(n * k log k)
- **Space Complexity:** O(nk)

```python
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for word in strs:
          key = "".join(sorted(word))
          groups[key].append(word)
        return list(groups.values())
```

<!-- AUTO-GENERATED END -->
