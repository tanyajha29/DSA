# Sliding_Window

Placement-focused revision notes for Sliding_Window.

## Problems

### 3. Longest Substring Without Repeating Characters (Medium)
LeetSync: [3-longest-substring-without-repeating-characters](../3-longest-substring-without-repeating-characters)

- **Pattern/Category:** Sliding Window
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Key Idea:** Track last seen index and shift window start when a repeat appears.

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] lastIndex = new int[256];
        for(int i=0; i<256; i++) lastIndex[i] = -1;

        int maxLen = 0, start = 0;
        for(int end = 0; end < s.length(); end++) {
            char c = s.charAt(end);
            if(lastIndex[c] >= start) start = lastIndex[c]+1;
            lastIndex[c] = end;
            maxLen = Math.max(maxLen, end - start + 1);
        }
        return maxLen;
    }
}

public class Main {
    public static void main(String[] args) {
        String s = "abcabcbb";
        int ret = new Solution().lengthOfLongestSubstring(s);
        System.out.println(ret); // Output: 3
    }
}
```

