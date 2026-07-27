# Arrays

Placement-focused revision notes for Arrays.

## Problems

<!-- AUTO-GENERATED START -->

### 61. Rotate List (Medium)

🔗 LeetCode Folder: [`61-rotate-list`](../61-rotate-list)

- **Pattern:** Arrays
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
    public ListNode rotateRight(ListNode head, int k) {

        if(head == null || head.next == null || k == 0){
            return head;
        }
        // 1. find the length of the list
        int length = 1;
        ListNode tail = head;

        while(tail.next != null){
            tail = tail.next;
            length++;
        }

        // 2. avoid unnecessary rotations
        k = k % length;

        if(k == 0){
            return head;
        }

        // 3. make the list circular
        tail.next = head;

        // 4. find new tail
        int steps = length - k - 1;
        ListNode newTail = head;

        for(int i = 0; i < steps; i++){
            newTail = newTail.next;
        }

        // 5. find new head
        ListNode newHead = newTail.next;

        // 6. break the node
        newTail.next = null;

        return newHead;
    }
}
```

### 80. Remove Duplicates From Sorted Array Ii (Medium)

🔗 LeetCode Folder: [`80-remove-duplicates-from-sorted-array-ii`](../80-remove-duplicates-from-sorted-array-ii)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length < 2){
            return nums.length;
        }

        int j = 2;
        for( int i = 2; i < nums.length; i++){
            if(nums[i] != nums[j - 2]){
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }
}
```

### 948. Sort An Array (Medium)

🔗 LeetCode Folder: [`948-sort-an-array`](../948-sort-an-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution:
    def mergeSort(self, nums, low, high) :
        if low >= high :
            return

        mid = (low + high) // 2
        self.mergeSort(nums, low, mid)
        self.mergeSort(nums, mid + 1, high)
        self.merge(nums, low, mid, high)

    def  merge(self, nums, low, mid, high) :
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high :
            if nums[left] <= nums[right] :
                temp.append(nums[left])
                left += 1
            else :
                temp.append(nums[right])
                right += 1

        while left <= mid :
            temp.append(nums[left])
            left += 1

        while right <= high :
            temp.append(nums[right])
            right += 1

        for i in range(low, high + 1) :
            nums[i] = temp[i - low]

        return nums

    def sortArray(self, nums):

        low = 0
        high = len(nums) - 1

        self.mergeSort(nums, low, high)

        return nums
```

### 1019. Squares Of A Sorted Array (Easy)

🔗 LeetCode Folder: [`1019-squares-of-a-sorted-array`](../1019-squares-of-a-sorted-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public int[] sortedSquares(int[] nums) {

        int index = nums.length - 1;
        int left = 0;
        int right = nums.length - 1;
        int[] ans = new int[nums.length];

        while(left <= right){
            int leftSquare = nums[left] * nums[left];
            int rightSquare = nums[right] * nums[right];

            if(leftSquare > rightSquare){
                ans[index] = leftSquare;
                left++;
            }
            else{
                ans[index] = rightSquare;
                right--;
            }
            index--;
        }
        return ans;
    }
}
```

<!-- AUTO-GENERATED END -->
