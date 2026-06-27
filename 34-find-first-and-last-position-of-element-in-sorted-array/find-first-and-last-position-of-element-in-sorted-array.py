class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)
        def firstOccurence(nums, n, target) :
            first = -1
            low = 0
            high = n - 1
            
            while low <= high :
                mid = (low + high)//2
                if nums[mid] == target :
                    first = mid
                    high = mid - 1
                elif nums[mid] < target :
                    low = mid + 1
                else :
                    high = mid -1
            
            return first

        def lastOccurence(nums, n, target) :
            last = -1
            low = 0
            high = n - 1
            
            while low <= high :
                mid = (low + high)//2
                if nums[mid] == target :
                    last = mid
                    low = mid + 1
                elif nums[mid] < target :
                    low = mid + 1
                else :
                    high = mid -1
            
            return last

        first = firstOccurence(nums, n, target)
        if first == -1 :
            return [-1, -1]
        
        last = lastOccurence(nums, n, target)
        return [first, last]
    