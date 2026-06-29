import math

class Solution:
    def find_sum(self, nums, m) :
        return sum(math.ceil(i/m) for i in nums)

    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if len(nums) > threshold :
            return -1

        low = 1
        high = max(nums)

        while low <= high :
            mid = (low + high)//2
            if (self.find_sum(nums, mid) <= threshold ) :
                high = mid - 1
            else :
                low = mid + 1
        
        return low
        
        