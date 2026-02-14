# Other Problem Solutions

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

### 12. Integer To Roman (Medium)

🔗 LeetCode Folder: [`12-integer-to-roman`](../../12-integer-to-roman)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public String intToRoman(int num) {
    int [] values={
        1000, 900, 500, 400,
        100,90, 50, 40,
        10,9,5,4,1
    };
    String[] symbols={"M","CM","D","CD",
    "C", "XC","L","XL",
    "X", "IX","V","IV","I"};

    StringBuilder res= new StringBuilder();

    for (int i=0 ;i<values.length; i++){
        while(num>= values[i]){
            res.append(symbols[i]);
            num-=values[i];
        }
    }    
    return res.toString();
    }
}
```

<!-- AUTO-GENERATED END -->
