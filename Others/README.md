# Others

Placement-focused revision notes for Others.

## Problems

<!-- AUTO-GENERATED START -->

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

<!-- AUTO-GENERATED END -->
