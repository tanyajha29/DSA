# Stack

Placement-focused revision notes for Stack.

## Problems

<!-- AUTO-GENERATED START -->

### 155. Min Stack (Medium)

🔗 LeetCode Folder: [`155-min-stack`](../155-min-stack)

- **Pattern:** Stack
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class MinStack {
    Stack<Integer> stack;
    Stack<Integer> minStack;

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if(minStack.isEmpty() || val <= minStack.peek()){
            minStack.push(val);
        }
    }
    
    public void pop() {
        int removed = stack.pop();
        if( removed == minStack.peek() ){
            minStack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```

### 983. Validate Stack Sequences (Medium)

🔗 LeetCode Folder: [`983-validate-stack-sequences`](../983-validate-stack-sequences)

- **Pattern:** Stack
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Stack<Integer> stack = new Stack<>();
        int j=0;

        for(int x : pushed){
            stack.push(x);

            while(!stack.isEmpty() && stack.peek()==popped[j]){
                stack.pop();
                j++;
            }
        }
        return stack.isEmpty();
    }
}
```

<!-- AUTO-GENERATED END -->
