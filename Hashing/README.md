# Hashing

Placement-focused revision notes for Hashing.

## Problems

### 1. Two Sum (Easy)
LeetSync: [1-two-sum](../1-two-sum)

- **Pattern/Category:** Hashing
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Key Idea:** Use a hash map to store value -> index and check complements.

```java
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> seen = new HashMap<>(); // value -> index

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }

            seen.put(nums[i], i);
        }

        // If no solution found (assume one solution always exists)
        return new int[]{-1, -1};
    }

    // Optional main to test
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = sol.twoSum(nums, target);

        System.out.println("Indices: [" + result[0] + ", " + result[1] + "]");
        // Output: Indices: [0, 1]
    }
}
```

### 49. Group Anagrams (Medium)
LeetSync: [49-group-anagrams](../49-group-anagrams)

- **Pattern/Category:** Sorting / Hashing
- **Time Complexity:** O(n * k log k)
- **Space Complexity:** O(nk)
- **Key Idea:** Sort each string to a canonical key and group together.

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        // Step 1: store original + sorted version
        String[][] arr = new String[strs.length][2];

        for (int i = 0; i < strs.length; i++) {
            char[] ch = strs[i].toCharArray();
            Arrays.sort(ch);
            arr[i][0] = strs[i];           // original
            arr[i][1] = new String(ch);    // sorted
        }

        // Step 2: sort based on sorted strings
        Arrays.sort(arr, (a, b) -> a[1].compareTo(b[1]));

        // Step 3: group adjacent anagrams
        List<List<String>> result = new ArrayList<>();

        for (int i = 0; i < arr.length; ) {
            List<String> group = new ArrayList<>();
            String key = arr[i][1];

            while (i < arr.length && arr[i][1].equals(key)) {
                group.add(arr[i][0]);
                i++;
            }

            result.add(group);
        }

        return result;
    }
}
```

