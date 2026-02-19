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