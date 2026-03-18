# Arrays

Placement-focused revision notes for Arrays.

## Problems

<!-- AUTO-GENERATED START -->

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

<!-- AUTO-GENERATED END -->
