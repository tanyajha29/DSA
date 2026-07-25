# Hashing

Placement-focused revision notes for Hashing.

## Problems

<!-- AUTO-GENERATED START -->

### 242. Valid Anagram (Easy)

🔗 LeetCode Folder: [`242-valid-anagram`](../242-valid-anagram)

- **Pattern:** Hashing
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        char[] arr1 = s.toLowerCase().toCharArray();
        char[] arr2 = t.toLowerCase().toCharArray();

        Arrays.sort(arr1);
        Arrays.sort(arr2);

        return Arrays.equals(arr1, arr2);

    }
}
```

<!-- AUTO-GENERATED END -->
