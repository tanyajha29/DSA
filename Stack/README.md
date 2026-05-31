# Stack

Placement-focused revision notes for Stack.

## Problems

<!-- AUTO-GENERATED START -->

### 232. Implement Queue Using Stacks (Easy)

🔗 LeetCode Folder: [`232-implement-queue-using-stacks`](../232-implement-queue-using-stacks)

- **Pattern:** Stack
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class MyQueue(object):

    def __init__(self):
        # initialize 2 array for storing and reversing the stack
        # 1. stack 1 which is for orginal elements storing
        self.instack = []

        #2. stack 2 will store the reversed elements from stack1
        self.outstack = []

    def push(self, x):
        #stor the element is stack 1
       self.instack.append(x)
        

    def pop(self):
        # check if there are elements in stack 2 or not
        self.peek()

        return self.outstack.pop()
        

    def peek(self):
        # store the elements in stack2 only if necessary 
        if not self.outstack :
            while self.instack :
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]
        

    def empty(self):
        return ( len(self.instack) == 0 and len(self.outstack) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

<!-- AUTO-GENERATED END -->
