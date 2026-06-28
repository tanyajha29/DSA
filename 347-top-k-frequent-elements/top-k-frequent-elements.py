class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for i in nums:
            # count frequency 
            # if key exist -> return value
            # else return 0
            freq[i] = freq.get(i, 0) + 1

            # sort the freq
            # according to values not key
            # sort them in decending instead of ascending order
            
        sorted_nums = sorted(freq, key = freq.get, reverse = True)
        # return 1st k elements
        return sorted_nums[:k]
    