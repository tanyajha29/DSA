class Solution(object):
    # funtion to check if the blooming is possible or not
    def possible(self, arr,day, m, k) :
        count = 0
        bouquets_formed = 0

        for i in range(len(arr)) :
            if arr[i] <= day :
                count += 1
            else :
                bouquets_formed += count // k 
                count = 0
            # last count tweak
        bouquets_formed += (count // k )

        return bouquets_formed >= m 

    def minDays(self, bloomDay, m, k):
        # not enough / base case
        if m * k > len(bloomDay) :
            return -1
        
        # binary search
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        while low <= high : 
            mid = (low + high)//2
            if self.possible(bloomDay, mid, m, k) :
                ans = mid
                high = mid - 1
            else: 
                low = mid + 1
        return ans

        