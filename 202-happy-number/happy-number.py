class Solution(object):
    def isHappy(self, n):

        seen = set()

        # loop until n becomes 1 or an endless loop is created
        while n != 1 and n not in seen:

            seen.add(n)
            total = 0

            # digit sqauare and addition
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return n == 1