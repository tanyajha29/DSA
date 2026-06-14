class Solution(object):
    def mySqrt(self, x):

        # initialize variable
        left = 0
        right = x
        result = 0

        # run binary search
        while left <= right :

            #compute mid
            mid = (right + left)//2
            square = mid * mid
            ''' If:
            mid² == x → return mid
            mid² < x → store answer, move right
            mid² > x → move left '''

            if square == x :
                return mid
            
            elif square < x :
                result = mid
                left = mid + 1
            
            else :
                right = mid -1 
        return result