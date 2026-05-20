# Arrays

Placement-focused revision notes for Arrays.

## Problems

<!-- AUTO-GENERATED START -->

### 121. Best Time To Buy And Sell Stock (Easy)

🔗 LeetCode Folder: [`121-best-time-to-buy-and-sell-stock`](../121-best-time-to-buy-and-sell-stock)

- **Pattern:** Greedy / One Pass
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

```python
class Solution(object):
    def maxProfit(self, prices):
        #declare and initialize variables
        min_pr=float('inf')
        max_pr=0

        #loop through all values/price
        for price in prices:
            # check and initalize min price
            if price < min_pr:
                min_pr = price
            #check profit and buy time
            profit = price - min_pr

            # check and initalize max price
            if profit > max_pr:
                max_pr = profit
        return max_pr
```

<!-- AUTO-GENERATED END -->
