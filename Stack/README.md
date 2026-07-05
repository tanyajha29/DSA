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

### 1737. Maximum Nesting Depth Of The Parentheses (Easy)

🔗 LeetCode Folder: [`1737-maximum-nesting-depth-of-the-parentheses`](../1737-maximum-nesting-depth-of-the-parentheses)

- **Pattern:** Stack
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def maxDepth(self, s):
        max_depth = 0
        curr_depth = 0
        
        for ch in s :
            if ch == "(" :
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            elif ch == ")":
                curr_depth -= 1
        return max_depth
```

<!-- AUTO-GENERATED END -->
