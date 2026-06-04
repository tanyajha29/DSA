class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # we need to check whether if array is in increasing or decreasing
        increasing = True
        decreasing = True

        #start from the second element of array
        for i in range(1, len(nums)) :

            #check whether incresing or decreasing
            if nums[i - 1] > nums[i] :
                decreasing = False
            
            if nums[i - 1] < nums[i] :
                increasing = False
        
        return increasing or decreasing
        