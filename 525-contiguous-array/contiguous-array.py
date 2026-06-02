class Solution(object):
    def findMaxLength(self, nums):
        # avariable with structure {prefix_sum : index}
        hashmap = {0 : -1}
        prefix_sum = 0
        max_len = 0
        for i in range( len(nums) ) :
            if nums [i] == 0 :
                prefix_sum -= 1
            else :
                prefix_sum += 1
            
            if prefix_sum in hashmap :
                length = i - hashmap[prefix_sum]
                max_len = max(length, max_len)
            else :
                hashmap[prefix_sum] = i
            
        return max_len
