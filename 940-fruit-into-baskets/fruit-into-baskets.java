class Solution {
    public int totalFruit(int[] fruits) {
        int left = 0;
        HashMap<Integer, Integer> basket = new HashMap<>();
        int maxTree = 0;

        for (int right = 0; right <fruits.length; right++){

            // add the fruit to the basket
            basket.put(fruits[right], basket.getOrDefault(fruits[right], 0)+1);

            // more that 2 types -> shrink
            while(basket.size() > 2){
                int leftFruit = fruits[left];
                
                basket.put(leftFruit, basket.get(leftFruit) - 1);
                if(basket.get(leftFruit) == 0){
                    basket.remove(leftFruit);
                }
                left++;
            }
            maxTree = Math.max(maxTree, right - left + 1);
        }
        return maxTree;
    }
}