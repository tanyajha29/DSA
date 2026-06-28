class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        //convert dictionary to hashset
        Set<String> resSet = new HashSet(wordDict);
        //create dp array
        boolean[] dp = new boolean[s.length() + 1];

        //initialize base array
        dp[0] = true;

        //fill dp array
        for(int i = 1; i <= s.length(); i++){
            for ( int j = 0; j < i; j++){
                if (dp[j] && resSet.contains(s.substring(j,i))){
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
}