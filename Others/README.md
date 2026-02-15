# Others

Placement-focused revision notes for Others.

## Problems

<!-- AUTO-GENERATED START -->

### 7. Reverse Integer (Medium)

🔗 LeetCode Folder: [`7-reverse-integer`](../7-reverse-integer)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public int reverse(int x) {
        int rev=0;

        while(x!=0){
            int digit=x%10;

            //positive overflow
            if(rev > Integer.MAX_VALUE/10||(rev==Integer.MAX_VALUE/10 && digit>7) )
            return 0;

            //negative overflow
             if( rev< Integer.MIN_VALUE/10||(rev==Integer.MIN_VALUE/10 && digit<-8) )
            return 0;


            rev= rev*10+digit;
            x=x/10;
        };
        return rev;
    }
}
```

### 9. Palindrome Number (Easy)

🔗 LeetCode Folder: [`9-palindrome-number`](../9-palindrome-number)

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

### 13. Roman To Integer (Easy)

🔗 LeetCode Folder: [`13-roman-to-integer`](../13-roman-to-integer)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public int romanToInt(String s) {
        int total=0;
        int prev=0;

        for(int i=s.length()-1;i>=0;i--){
            int curr= value(s.charAt(i));

            if(curr<prev){
                total-=curr;
            }else{
                total+=curr;
            }

            prev=curr;
        }
        return total;
    }
    private int value(char c){
        switch (c){
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
        }
        return 0;
    }
}
```

<!-- AUTO-GENERATED END -->
