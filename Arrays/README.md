# Arrays

Placement-focused revision notes for Arrays.

## Problems

<!-- AUTO-GENERATED START -->

### 26. Remove Duplicates From Sorted Array (Easy)

🔗 LeetCode Folder: [`26-remove-duplicates-from-sorted-array`](../26-remove-duplicates-from-sorted-array)

- **Pattern:** Arrays
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        //chect if null
        if( nums.length==0){
            return 0;
        }

        int i=0;
        for(int j=1;j<nums.length;j++){
            if(nums[j]!=nums[i]){
                i++;
                nums[i]=nums[j];
            }
        }
        return i+1;
    }
}
```

<!-- AUTO-GENERATED END -->
