# Arrays

Placement-focused revision notes for Arrays.

## Problems

<!-- AUTO-GENERATED START -->

### 26. Remove Duplicates From Sorted Array (Easy)

🔗 LeetCode Folder: [`26-remove-duplicates-from-sorted-array`](../26-remove-duplicates-from-sorted-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

_No solution file found in the LeetSync folder._

### 33. Search In Rotated Sorted Array (Medium)

🔗 LeetCode Folder: [`33-search-in-rotated-sorted-array`](../33-search-in-rotated-sorted-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            # target found
            if nums[mid] == target:
                return mid

            # LEFT HALF SORTED
            if nums[left] <= nums[mid]:

                # target inside left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # RIGHT HALF SORTED
            else:

                # target inside right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
```

### 88. Merge Sorted Array (Easy)

🔗 LeetCode Folder: [`88-merge-sorted-array`](../88-merge-sorted-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1; //valid last element of num1
        int j = n - 1; //last element of nums2
        int k = m + n -1; //last element of num1

        //itetrate till one array has no element to itetrate
        while (i >= 0 && j >= 0){
            if (nums1[i] > nums2[j]){
                nums1[k] = nums1[i];
                i--;
            }else{
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        }
        //if nums2 still hast elements left
        while(j >= 0){
            nums1[k] = nums2[j];
            j--;
            k--;
        }
    }
}
```

### 121. Best Time To Buy And Sell Stock (Easy)

🔗 LeetCode Folder: [`121-best-time-to-buy-and-sell-stock`](../121-best-time-to-buy-and-sell-stock)

- **Pattern:** Greedy / One Pass
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

```python
class Solution(object):
    def maxProfit(self, prices):
        #declare and initialize variables
        min_pr=float('inf')
        max_pr=0

        #loop through all values/price
        for price in prices:
            # check and initalize min price
            if price < min_pr:
                min_pr = price
            #check profit and buy time
            profit = price - min_pr

            # check and initalize max price
            if profit > max_pr:
                max_pr = profit
        return max_pr
```

<!-- AUTO-GENERATED END -->
