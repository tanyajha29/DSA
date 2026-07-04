class Solution(object):
    def reverseWords(self, s):
        n = len(s) - 1
        result = ""
        while n >= 0 :
            while n >= 0 and s[n] == " " :
                n -= 1

            if n < 0 :
                break

            end = n
            while n >= 0 and s[n] != " " :
                n -= 1

            word = s[n + 1: end + 1]
            if result != "" :
                result += " "

            result += word

        return result
        