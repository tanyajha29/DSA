class Solution {
    public List<List<Integer>> generate(int numRows) {
        //create an empty list result
        List<List<Integer>> result = new ArrayList<>();

        //loop from 0 to numrows-1
        for (int i = 0; i < numRows; i++){
            //make a new List
            List<Integer> row = new ArrayList<>();
            //add 1 at the start
            row.add(1);

            //fill middle using previous row
            for(int j = 1; j < i; j++){
                //calculate middle value
                int val = result.get(i - 1).get(j - 1)+result.get(i - 1).get(j);
                row.add(val);
            }
            //add 1 at the last
            if(i > 0){
                row.add(1);
            }
            result.add(row);
        }
        return result;
    }
}