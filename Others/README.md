# Others

Placement-focused revision notes for Others.

## Problems

<!-- AUTO-GENERATED START -->

### 112. Path Sum (Easy)

🔗 LeetCode Folder: [`112-path-sum`](../112-path-sum)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        //check if null
        if(root == null){
            return false;
        }

        //if we reach leaf node
        if(root.left == null && root.right == null){
            //check if remSum = targetsum
            return targetSum == root.val;
        }

        //subtrack current node from targetsum
        int remSum = targetSum - root.val;
        //move to left or right child
        return hasPathSum(root.left , remSum) || hasPathSum(root.right, remSum); 
    }
}
```

### 118. Pascals Triangle (Easy)

🔗 LeetCode Folder: [`118-pascals-triangle`](../118-pascals-triangle)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public List<List<Integer>> generate(int numRows) {
        //create an empty list result
        List<List<Integer>> result = new ArrayList<>();

        //loop from 0 to numrows-1
        for (int i = 0; i < numRows; i++){
            //make a new List
            List<Integer> row = new ArrayList<>();
            //add 1 at the start
            row.add(1);

            //fill middle using previous row
            for(int j = 1; j < i; j++){
                //calculate middle value
                int val = result.get(i - 1).get(j - 1)+result.get(i - 1).get(j);
                row.add(val);
            }
            //add 1 at the last
            if(i > 0){
                row.add(1);
            }
            result.add(row);
        }
        return result;
    }
}
```

### 125. Valid Palindrome (Easy)

🔗 LeetCode Folder: [`125-valid-palindrome`](../125-valid-palindrome)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public boolean isPalindrome(String s) {
        //two pointers
        int left = 0; //start
        int right = s.length() -1; //end

        while(left < right)
        {
             //skip non alphanumeric character
             while(left < right && !Character.isLetterOrDigit(s.charAt(left))){
                left++;
             }
             while(left < right && !Character.isLetterOrDigit(s.charAt(right))){
                right--;
             }
             //move pointers on match else return false
             if(Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))){
                return false;
             }
             left++;
             right--;
        }
        return true;
    }
}
```

### 139. Word Break (Medium)

🔗 LeetCode Folder: [`139-word-break`](../139-word-break)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        //convert dictionary to hashset
        Set<String> resSet = new HashSet(wordDict);
        //create dp array
        boolean[] dp = new boolean[s.length() + 1];

        //initialize base array
        dp[0] = true;

        //fill dp array
        for(int i = 1; i <= s.length(); i++){
            for ( int j = 0; j < i; j++){
                if (dp[j] && resSet.contains(s.substring(j,i))){
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
}
```

### 387. First Unique Character In A String (Easy)

🔗 LeetCode Folder: [`387-first-unique-character-in-a-string`](../387-first-unique-character-in-a-string)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public int firstUniqChar(String s) {
        int[] freq = new int[26];

        //count frequency
        for(int i = 0; i < s.length(); i++){
            freq[s.charAt(i) - 'a']++;
        }

        //find first unique character
         for(int i = 0; i < s.length(); i++){
           if(freq[s.charAt(i) - 'a'] == 1){
            return i;
           }
         }
         return -1;
    }
}
```

<!-- AUTO-GENERATED END -->
