# Others

Placement-focused revision notes for Others.

## Problems

<!-- AUTO-GENERATED START -->

### 35. Search Insert Position (Easy)

🔗 LeetCode Folder: [`35-search-insert-position`](../35-search-insert-position)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;
        while(left<=right){
            int mid = left + (right-left)/2;
            if (nums[mid] == target){
                return mid;
            }
            else if( nums[mid] < target){
                left = mid +1;
            }
            else{
                right = mid-1;
            }
        }
        return left;
    }
}
```

### 58. Length Of Last Word (Easy)

🔗 LeetCode Folder: [`58-length-of-last-word`](../58-length-of-last-word)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public int lengthOfLastWord(String s) {
        int len = 0;
        int i = s.length() - 1;
        while ( i >= 0 && s.charAt(i) == ' '){
            i--;
        }
         while ( i >= 0 && s.charAt(i) != ' '){
            len++;
            i--;
        }
        return len;
    }
}
```

### 66. Plus One (Easy)

🔗 LeetCode Folder: [`66-plus-one`](../66-plus-one)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length-1; i >=0; i--){
            if( digits[i] < 9){
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        int[] result = new int[digits.length + 1];
        result[0] =1;
        return result;
    }
}
```

<!-- AUTO-GENERATED END -->
