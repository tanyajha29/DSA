class Solution(object):
    def validPalindrome(self, s):
        def check_after_skipping(left, right) :
            while left < right :
                if s[left] != s[right] :
                    return False
                left += 1
                right -= 1
            return True 

        left , right = 0, len(s) - 1
        while left < right :
            if s[left] != s[right] :
                return check_after_skipping(left + 1, right) or check_after_skipping(left, right - 1)
            left += 1
            right -= 1
        return True
    
    