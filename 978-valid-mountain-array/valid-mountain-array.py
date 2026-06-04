class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i = 0
        n = len(arr)
        
        # increasing order till peak
        while i < n - 1 and arr[i] < arr[i + 1] :
            i += 1
        
        # peak cannot be at start or end
        if i == 0 or i == n - 1 :
            return False

        # decreasing order after peak
        while i < n - 1 and arr[i] > arr[i + 1] :
            i += 1

        # must reach end
        return i == n - 1