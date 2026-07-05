# Stack

Placement-focused revision notes for Stack.

## Problems

<!-- AUTO-GENERATED START -->

### 1078. Remove Outermost Parentheses (Easy)

🔗 LeetCode Folder: [`1078-remove-outermost-parentheses`](../1078-remove-outermost-parentheses)

- **Pattern:** Stack
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def removeOuterParentheses(self, s):
        res = []
        balance = 0
        for ch in s :
            # If you see '(' and current balance > 0, add it to the answer.
            if ch == '(' :
                if balance > 0 :
                    res.append(ch)
                
                # Then increase balance.
                balance += 1
            else :
                # If you see ')', decrease balance first.
                balance -= 1

                # If balance > 0 after decreasing, add it to the answer.
                if balance > 0 :
                    res.append(ch)

        return "".join(res)
```

<!-- AUTO-GENERATED END -->
