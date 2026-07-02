class Solution(object):
    def reverseVowels(self, s):
        left = 0
        right = len(s) - 1
        s = list(s)
        vowels = set("aeiouAEIOU")

        while left < right :
            while left < right and s[left] not in vowels :
                left += 1
            
            while left < right and s[right] not in vowels :
                right -= 1

            s[right], s[left] = s[left], s[right]
            left += 1
            right -= 1

        return "".join(s)
        