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