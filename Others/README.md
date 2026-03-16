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

<!-- AUTO-GENERATED END -->
