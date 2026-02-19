# Others

Placement-focused revision notes for Others.

## Problems

<!-- AUTO-GENERATED START -->

### 27. Remove Element (Easy)

🔗 LeetCode Folder: [`27-remove-element`](../27-remove-element)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public int removeElement(int[] nums, int val) {

        int i=0;

        for(int j=0;j<nums.length;j++){
            if(nums[j]!=val){
                nums[i]=nums[j];
                i++;
            }
        }
        return i;
    }
}
```

<!-- AUTO-GENERATED END -->
