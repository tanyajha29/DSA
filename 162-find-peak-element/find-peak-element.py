class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        # base case 
        # if array has a single element
        if n == 1 :
            return 0
        
        # if 1st element is the peak
        elif nums[0] > nums[1] :
            return 0

        # if last element is the peak
        elif nums[n - 1] > nums[n - 2] :
            return(n - 1)
        
        # binary search
        low = 1
        high = n - 1

        while low <= high :
            mid = (low + high) // 2 
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1] :
                return mid
            elif nums[mid] > nums[mid - 1] :
                low = mid + 1
            else :
                high = mid - 1
        return -1