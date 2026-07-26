# Hashing

Placement-focused revision notes for Hashing.

## Problems

<!-- AUTO-GENERATED START -->

### 49. Group Anagrams (Medium)

🔗 LeetCode Folder: [`49-group-anagrams`](../49-group-anagrams)

- **Pattern:** Sorting / Hashing
- **Time Complexity:** O(n * k log k)
- **Space Complexity:** O(nk)

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        HashMap<String, List<String>> map = new HashMap<>();

        for(String s : strs){
            char[] ch = s.toCharArray();
            Arrays.sort(ch);

            String key = new String(ch);
            if(!map.containsKey(key)){
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
```

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
