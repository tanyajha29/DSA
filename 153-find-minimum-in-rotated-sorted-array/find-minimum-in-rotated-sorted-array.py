class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1
        result = nums[0]

        while low <= high :
            mid = (low + high) // 2
            # if left half is sorted
            if nums[low] <= nums[mid] :
                result = min(result, nums[low])
                low = mid + 1
            # if right half is sorted
            else:
                high = mid -  1
                result = min(result, nums[mid])

        return result
        