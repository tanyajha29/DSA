# Arrays

Placement-focused revision notes for Arrays.

## Problems

### 121. Best Time to Buy and Sell Stock (Unknown)
🔗 LeetSync: [121-best-time-to-buy-and-sell-stock](../121-best-time-to-buy-and-sell-stock)

- **Pattern/Category:** Greedy / One Pass
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Key Idea:** Track minimum price so far and maximize profit.

```java
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit=0;
        for ( int i=0;i<prices.length; i++){
            if(prices[i]<minPrice){
                minPrice=prices[i];
            }else{
                int profit= prices[i]-minPrice;
                maxProfit=Math.max(maxProfit, profit);
            }
        }
            return maxProfit;
        }
        
    
}
```

### 238. Product of Array Except Self (Unknown)
🔗 LeetSync: [238-product-of-array-except-self](../238-product-of-array-except-self)

- **Pattern/Category:** Prefix / Suffix
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Key Idea:** Build prefix products then multiply by running suffix product.

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];

        // Step 1: prefix product
        answer[0] = 1;
        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }

        // Step 2: multiply with suffix product
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= suffix;
            suffix *= nums[i];
        }

        return answer;
    }
}
```

