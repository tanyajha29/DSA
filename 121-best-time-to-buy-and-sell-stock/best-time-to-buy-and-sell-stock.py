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