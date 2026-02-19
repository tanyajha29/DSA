# Others

Placement-focused revision notes for Others.

## Problems

<!-- AUTO-GENERATED START -->

### 27. Remove Element (Easy)

🔗 LeetCode Folder: [`27-remove-element`](../27-remove-element)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public int removeElement(int[] nums, int val) {

        int i=0;

        for(int j=0;j<nums.length;j++){
            if(nums[j]!=val){
                nums[i]=nums[j];
                i++;
            }
        }
        return i;
    }
}
```

### 28. Find The Index Of The First Occurrence In A String (Easy)

🔗 LeetCode Folder: [`28-find-the-index-of-the-first-occurrence-in-a-string`](../28-find-the-index-of-the-first-occurrence-in-a-string)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
//using haystack

class Solution {
    
    public int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }
}


/*class Solution {
    // 1. Changed method name from 'find' to 'strStr' to match the Driver
    public int strStr(String haystack, String needle) {

        if (needle.length() == 0) return 0;

        // 2. Added <= so you don't skip the very last possible match position
        for (int j = 0; j <= haystack.length() - needle.length(); j++) {
            int i = 0;

            // 3. Use .length() and .charAt() for Strings
            while (i < needle.length() && haystack.charAt(j + i) == needle.charAt(i)) {
                i++;
            }

            // 4. Return 'j' (the starting index), not 'i' (the length of the match)
            if (i == needle.length()) return j;
        }
        return -1;
    }
}*/
```

<!-- AUTO-GENERATED END -->
