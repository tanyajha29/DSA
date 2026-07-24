# Arrays

Placement-focused revision notes for Arrays.

## Problems

<!-- AUTO-GENERATED START -->

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

<!-- AUTO-GENERATED END -->
