class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0

        # traverse the array
        for i in nums :
            if count == 0 :
                candidate = i
            
            if i == candidate :
                count += 1
            else :
                count -= 1

        return candidate
        