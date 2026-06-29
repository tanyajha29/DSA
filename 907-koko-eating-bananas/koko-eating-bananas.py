import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # function to calculate hours
        def calculateHour( piles, speed) :
            hrs = 0
            for i in piles :
                hrs += math.ceil( i/speed )
            
            return hrs

        # binary Search
        high = max(piles)
        low = 1
        result = high
        
        while low <= high :
            mid = (low + high)//2
            total_hour = calculateHour(piles, mid)

            # check the hour value
            if total_hour <= h :
                result = mid
                high = mid - 1
            else :
                low = mid + 1
        return result
        