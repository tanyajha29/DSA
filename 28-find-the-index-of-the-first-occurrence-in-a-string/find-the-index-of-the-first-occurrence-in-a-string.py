class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)

        for i in range (len(haystack) - n + 1):
            # check substring
            if haystack[ i : i + n] == needle:
                return i
        return -1
        