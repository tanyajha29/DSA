from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):

        freq = Counter(s)
        ans = 0

        for i in freq.values() :
            ans += (i//2) * 2

        if ans < len(s) :
            ans += 1
        
        return ans
