class Solution(object):
    def majorityElement(self, nums):
        element1 = None
        element2 = None
        count1 = 0
        count2 = 0

        for i in nums :
            if i == element1 :
                count1 += 1
            elif i == element2 :
                count2 += 1
            elif count1 == 0 :
                element1 = i
                count1 = 1
            elif count2 == 0 :
                element2 = i
                count2 = 1
            else :
                count1 -= 1
                count2 -= 1
        
        count1 = 0
        count2 = 0
        for j in nums :
            if j == element1 :
                count1 += 1
            elif j == element2 :
                count2 += 1
        
        result = []
        n = len(nums)
        if count1 > n//3 :
            result.append(element1)
        
        if count2 > n//3 :
            result.append(element2)

        return result
        