# Others

DSA revision notes for Others.

## Problems

<!-- AUTO-GENERATED START -->

### 9. Palindrome Number (Easy)

🔗 LeetCode Folder: [`9-palindrome-number`](../../9-palindrome-number)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public boolean isPalindrome(int x) {
        int rev=0;
        int org=x;
        if (x<0) return false;
        while(x!=0){
            int digit=x%10;
             rev=rev*10+digit;
             x=x/10;
        }
        return org==rev;
    }
}
```

<!-- AUTO-GENERATED END -->
