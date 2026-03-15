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

### 232. Implement Queue Using Stacks (Easy)

🔗 LeetCode Folder: [`232-implement-queue-using-stacks`](../232-implement-queue-using-stacks)

- **Pattern:** Stack
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class MyQueue {
    Stack<Integer> stack1;
    Stack<Integer> stack2;

    public MyQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }
    
    public void push(int x) {
        stack1.push(x);
    }
    
    public int pop() {
        peek();
        return stack2.pop();
    }
    
    public int peek() {
        if(stack2.isEmpty()){
            while (!stack1.isEmpty()){
                stack2.push(stack1.pop());
            }
        }
        return stack2.peek();
    }
    
    public boolean empty() {
        return stack1.isEmpty() && stack2.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
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

### 1552. Build An Array With Stack Operations (Medium)

🔗 LeetCode Folder: [`1552-build-an-array-with-stack-operations`](../1552-build-an-array-with-stack-operations)

- **Pattern:** Stack
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> res= new ArrayList<>();
        int j=0;

        for (int i=1; i<=n && j < target.length; i++){
            if ( i == target[j]){
                res.add("Push");
                j++;
            }
            else{
                res.add("Push");
                res.add("Pop");
            }
        }
        return res;
    }
}
```

<!-- AUTO-GENERATED END -->
