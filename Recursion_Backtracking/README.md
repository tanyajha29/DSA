# Recursion_Backtracking

Placement-focused revision notes for Recursion_Backtracking.

## Problems

<!-- AUTO-GENERATED START -->

### 40. Combination Sum Ii (Medium)

🔗 LeetCode Folder: [`40-combination-sum-ii`](../40-combination-sum-ii)

- **Pattern:** Backtracking
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result=new ArrayList<>();
        findCombination(candidates, target,0, new ArrayList<>(),  result);
        return result;
        
    }

   public void findCombination(int[] candidates, int target,int start, List<Integer> curr,  List<List<Integer>> result){
        if(target==0) {
            result.add(new ArrayList<>(curr));
            return;
        }
        if(target<0) return;

        for(int i=start;i<candidates.length;i++){

            //skip duplicates
            if(i>start && candidates[i]==candidates[i-1])
            continue;

            curr.add(candidates[i]);
            findCombination(candidates, target-candidates[i],i+1, curr, result);
            curr.remove(curr.size()-1);
        }
    }
}
```

### 78. Subsets (Medium)

🔗 LeetCode Folder: [`78-subsets`](../78-subsets)

- **Pattern:** Backtracking
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result=new ArrayList<>();
        findSubset(nums, 0, new ArrayList<>(), result);
        return result;
    }

    //recursive function
    public void findSubset(int[] nums, int start,List<Integer> combinations,  List<List<Integer>> result){
        
            result.add(new ArrayList<>(combinations));

        for(int i=start; i< nums.length; i++){
            combinations.add(nums[i]);
            findSubset(nums, i+1, combinations, result);

        combinations.remove(combinations.size()-1);

        }
    }
}
```

<!-- AUTO-GENERATED END -->
