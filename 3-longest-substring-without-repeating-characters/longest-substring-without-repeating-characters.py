class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_len = 0
        seen = set()

        for right in range (len(s)):
            # check duplicates
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max( max_len, right - left +1)
        return max_len
        