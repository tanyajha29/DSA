class Solution(object):
    def rearrangeArray(self, nums):
        negIndex = 1
        posIndex = 0
        n = len(nums)
        result = [0] * n

        for i in range (n) :
            if nums[i] < 0 :
                result[negIndex] = nums[i]
                negIndex += 2
            else :
                result[posIndex] = nums[i]
                posIndex += 2
        return result