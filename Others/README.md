# Others

Placement-focused revision notes for Others.

## Problems

<!-- AUTO-GENERATED START -->

### 23. Merge K Sorted Lists (Hard)

🔗 LeetCode Folder: [`23-merge-k-sorted-lists`](../23-merge-k-sorted-lists)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    # merge two sorted lists
    def mergeTwoLists(self, l1, l2):

        dummy = ListNode(0)

        tail = dummy

        while l1 and l2:

            if l1.val < l2.val:

                tail.next = l1
                l1 = l1.next

            else:

                tail.next = l2
                l2 = l2.next

            tail = tail.next

        # remaining nodes
        if l1:
            tail.next = l1

        else:
            tail.next = l2

        return dummy.next

    def mergeKLists(self, lists):

        if not lists:
            return None

        # keep merging until one list remains
        while len(lists) > 1:

            mergedLists = []

            # merge in pairs
            for i in range(0, len(lists), 2):

                l1 = lists[i]

                # second list may not exist
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                mergedLists.append(
                    self.mergeTwoLists(l1, l2)
                )

            lists = mergedLists

        return lists[0]
```

### 28. Find The Index Of The First Occurrence In A String (Easy)

🔗 LeetCode Folder: [`28-find-the-index-of-the-first-occurrence-in-a-string`](../28-find-the-index-of-the-first-occurrence-in-a-string)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)

        for i in range (len(haystack) - n + 1):
            # check substring
            if haystack[ i : i + n] == needle:
                return i
        return -1
```

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

### 45. Jump Game Ii (Medium)

🔗 LeetCode Folder: [`45-jump-game-ii`](../45-jump-game-ii)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

_No solution file found in the LeetSync folder._

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

### 62. Unique Paths (Medium)

🔗 LeetCode Folder: [`62-unique-paths`](../62-unique-paths)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1] * n for _ in range(m)]

        for i in range (1, m) :
            for j in range(1, n) :
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            
        return dp[m-1][n-1]
```

### 63. Unique Paths Ii (Medium)

🔗 LeetCode Folder: [`63-unique-paths-ii`](../63-unique-paths-ii)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 :
            return 0

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for i in range(m) :
            for j in range(n) :
                if obstacleGrid[i][j] == 1 :
                    dp[i][j] = 0
                else :
                    # from top
                    if i > 0 :
                          dp[i][j] += dp[i -1][j]
                    if j > 0 :
                        dp[i][j] += dp[i][j - 1]
        
        return dp[m-1][n-1]
```

### 64. Minimum Path Sum (Medium)

🔗 LeetCode Folder: [`64-minimum-path-sum`](../64-minimum-path-sum)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        
        # fill the starting cell
        dp[0][0] = grid[0][0]
        
        # fill first row 
        for j in range(1, n) :
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # fill first column
        for i in range(1, m) :
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # fill ramaining columns
        for i in range(1, m) :
            for j in range(1, n) :
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[m-1][n-1]
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

### 67. Add Binary (Easy)

🔗 LeetCode Folder: [`67-add-binary`](../67-add-binary)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):

    def addBinary(self, a, b):

        i = len(a) - 1
        j = len(b) - 1

        carry = 0

        result = []

        while i >= 0 or j >= 0 or carry:

            total = carry

            # add from a
            if i >= 0:
                total += int(a[i])
                i -= 1

            # add from b
            if j >= 0:
                total += int(b[j])
                j -= 1

            # current binary digit
            result.append(str(total % 2))

            # update carry
            carry = total // 2

        # reverse because built backwards
        return "".join(result[::-1])
```

### 69. Sqrtx (Easy)

🔗 LeetCode Folder: [`69-sqrtx`](../69-sqrtx)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def mySqrt(self, x):

        # initialize variable
        left = 0
        right = x
        result = 0

        # run binary search
        while left <= right :

            #compute mid
            mid = (right + left)//2
            square = mid * mid
            ''' If:
            mid² == x → return mid
            mid² < x → store answer, move right
            mid² > x → move left '''

            if square == x :
                return mid
            
            elif square < x :
                result = mid
                left = mid + 1
            
            else :
                right = mid -1 
        return result
```

### 70. Climbing Stairs (Easy)

🔗 LeetCode Folder: [`70-climbing-stairs`](../70-climbing-stairs)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def climbStairs(self, n):
        if n == 1 :
            return 1
        
        if n == 2 :
            return 2
        
        first = 1
        second = 2

        for i in range (3, n + 1) :
            current = first + second
            first = second
            second = current
        
        return second
```

### 75. Sort Colors (Medium)

🔗 LeetCode Folder: [`75-sort-colors`](../75-sort-colors)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def sortColors(self, nums):
        low = 0
        mid = 0
        n = len(nums)
        high = n - 1

        for i in range(n) :
            if nums[mid] == 0 :
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            elif nums[mid] == 1 :
                mid += 1
            elif nums[mid] == 2 :
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

### 83. Remove Duplicates From Sorted List (Easy)

🔗 LeetCode Folder: [`83-remove-duplicates-from-sorted-list`](../83-remove-duplicates-from-sorted-list)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode curr = head;

        //start from head
        while(curr != null && curr.next != null){
            if (curr.val == curr.next.val){
                curr.next = curr.next.next;
            }else{
                curr = curr.next;
            }
        }
        return head;
    }
}
```

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

### 169. Majority Element (Easy)

🔗 LeetCode Folder: [`169-majority-element`](../169-majority-element)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0

        # traverse the array
        for i in nums :
            if count == 0 :
                candidate = i
            
            if i == candidate :
                count += 1
            else :
                count -= 1

        return candidate
```

### 202. Happy Number (Easy)

🔗 LeetCode Folder: [`202-happy-number`](../202-happy-number)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def isHappy(self, n):

        seen = set()

        # loop until n becomes 1 or an endless loop is created
        while n != 1 and n not in seen:

            seen.add(n)
            total = 0

            # digit sqauare and addition
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return n == 1
```

### 217. Contains Duplicate (Easy)

🔗 LeetCode Folder: [`217-contains-duplicate`](../217-contains-duplicate)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
```

### 229. Majority Element Ii (Medium)

🔗 LeetCode Folder: [`229-majority-element-ii`](../229-majority-element-ii)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def majorityElement(self, nums):
        element1 = None
        element2 = None
        count1 = 0
        count2 = 0

        for i in nums :
            if i == element1 :
                count1 += 1
            elif i == element2 :
                count2 += 1
            elif count1 == 0 :
                element1 = i
                count1 = 1
            elif count2 == 0 :
                element2 = i
                count2 = 1
            else :
                count1 -= 1
                count2 -= 1
        
        count1 = 0
        count2 = 0
        for j in nums :
            if j == element1 :
                count1 += 1
            elif j == element2 :
                count2 += 1
        
        result = []
        n = len(nums)
        if count1 > n//3 :
            result.append(element1)
        
        if count2 > n//3 :
            result.append(element2)

        return result
```

### 268. Missing Number (Easy)

🔗 LeetCode Folder: [`268-missing-number`](../268-missing-number)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        exp_sum = (n*(n + 1))//2
        actual_sum = sum(nums)

        return exp_sum - actual_sum
```

### 283. Move Zeroes (Easy)

🔗 LeetCode Folder: [`283-move-zeroes`](../283-move-zeroes)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
```

### 344. Reverse String (Easy)

🔗 LeetCode Folder: [`344-reverse-string`](../344-reverse-string)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

### 347. Top K Frequent Elements (Medium)

🔗 LeetCode Folder: [`347-top-k-frequent-elements`](../347-top-k-frequent-elements)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for i in nums:
            # count frequency 
            # if key exist -> return value
            # else return 0
            freq[i] = freq.get(i, 0) + 1

            # sort the freq
            # according to values not key
            # sort them in decending instead of ascending order
            
        sorted_nums = sorted(freq, key = freq.get, reverse = True)
        # return 1st k elements
        return sorted_nums[:k]
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

### 485. Max Consecutive Ones (Easy)

🔗 LeetCode Folder: [`485-max-consecutive-ones`](../485-max-consecutive-ones)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        count = 0
        for i in range(len(nums)) :
            if nums[i] == 1 :
                count += 1
                max_count = max(max_count, count)
            else :
                count = 0
        return max_count
```

### 493. Reverse Pairs (Hard)

🔗 LeetCode Folder: [`493-reverse-pairs`](../493-reverse-pairs)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def reversePairs(self, nums):

        # count reverse pairs
        def count_pair(nums, low, mid, high):
            count = 0
            right = mid + 1

            for i in range(low, mid + 1):
                while right <= high and nums[i] > 2 * nums[right]:
                    right += 1

                count += right - (mid + 1)

            return count

        # merge function
        def merge(nums, low, mid, high):
            temp = []

            left = low
            right = mid + 1

            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1

            while left <= mid:
                temp.append(nums[left])
                left += 1

            while right <= high:
                temp.append(nums[right])
                right += 1

            for i in range(low, high + 1):
                nums[i] = temp[i - low]

        # divide and recursive calls
        def mergesort(nums, low, high):

            if low >= high:
                return 0

            mid = (low + high) // 2

            count = mergesort(nums, low, mid)
            count += mergesort(nums, mid + 1, high)

            count += count_pair(nums, low, mid, high)

            merge(nums, low, mid, high)

            return count

        return mergesort(nums, 0, len(nums) - 1)
```

### 792. Binary Search (Easy)

🔗 LeetCode Folder: [`792-binary-search`](../792-binary-search)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while right >= left :
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        return -1
```

### 1626. Can Make Arithmetic Progression From Sequence (Easy)

🔗 LeetCode Folder: [`1626-can-make-arithmetic-progression-from-sequence`](../1626-can-make-arithmetic-progression-from-sequence)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(2, len(arr)) :
            if arr[i] - arr[i - 1] != diff :
                return False
        
        return True
```

<!-- AUTO-GENERATED END -->
