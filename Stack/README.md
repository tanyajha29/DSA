# Stack

Placement-focused revision notes for Stack.

## Problems

### 20. Valid Parentheses (Unknown)
🔗 LeetSync: [20-valid-parentheses](../20-valid-parentheses)

- **Pattern/Category:** Stack
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Key Idea:** Push opening brackets and match with closing brackets.

```java
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack=new Stack<>();
        for (char ch:s.toCharArray()){
            if(ch=='('||ch=='['||ch=='{'){
                stack.push(ch);
            }
            else{
                if(stack.isEmpty())return false;
                char top=stack.pop();
                if(ch==')'&& top!='(') return false;
                 if(ch==']'&& top!='[') return false;
                  if(ch=='}'&& top!='{') return false;

            }
        }
        return stack.isEmpty();
        
    }
}
```

### 84. Largest Rectangle in Histogram (Unknown)
🔗 LeetSync: [84-largest-rectangle-in-histogram](../84-largest-rectangle-in-histogram)

- **Pattern/Category:** Monotonic Stack
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Key Idea:** Maintain increasing stack; compute area when a shorter bar appears.

```java
class Solution {
    public int largestRectangleArea(int[] heights) {
         Stack<Integer> stack = new Stack<>();
        int maxArea=0;
        int n=heights.length;
        for(int i=0;i<=n;i++){
            int currHeight=(i==n)?0:heights[i];
            while (!stack.isEmpty()&& currHeight<heights[stack.peek()]){
                int height=heights[stack.pop()];
                int width=stack.isEmpty()?i:i-stack.peek()-1;
                maxArea=Math.max(maxArea, height*width);

            }
            stack.push(i);
        }
        return maxArea;
    }
}
```

