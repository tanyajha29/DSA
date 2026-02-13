# Two_Pointers

Placement-focused revision notes for Two_Pointers.

## Problems

### 11. Container With Most Water (Medium)
LeetSync: [11-container-with-most-water](../11-container-with-most-water)

- **Pattern/Category:** Two Pointers
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Key Idea:** Move the pointer at the shorter height to improve area.

```java
class Solution {
    public int maxArea(int[] height) {

        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {

            int width = right - left;
            int minHeight = Math.min(height[left], height[right]);
            int area = width * minHeight;

            maxArea = Math.max(maxArea, area);

            // move smaller height pointer
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
}
```

### 15. 3Sum (Medium)
LeetSync: [15-3sum](../15-3sum)

- **Pattern/Category:** Sorting + Two Pointers
- **Time Complexity:** O(n^2)
- **Space Complexity:** O(1)
- **Key Idea:** Sort the array, fix i, and use two pointers while skipping duplicates.

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {

            // duplicate i skip
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {

                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    // skip duplicates
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;

                    left++;
                    right--;

                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }
}
```

