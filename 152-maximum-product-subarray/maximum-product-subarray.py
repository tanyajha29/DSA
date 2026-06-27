class Solution(object):
    def maxProduct(self, nums):
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in nums[1:] :
            if i < 0 :
                # why swap
                '''multiplying by -ve number flips sign'''
                max_product, min_product = min_product, max_product
            
            max_product = max(i, max_product * i)
            min_product = min(i, min_product * i)
            result = max(result, max_product)

        return result