class Solution(object):
    def arrayNesting(self, nums):
        # to track processed elements.
        visited = set()
        max_len = 0

        '''Loop through every index.
        If already visited: skip.'''

        for i in range( len(nums) ) :
            if i in visited :
                continue
            
            #start traversal from current index.
            count = 0
            current = i

            '''While current not visited:mark visited
            move to next index
            increase count'''

            while current not in visited :
                visited.add(current)

                #jump to next index
                current = nums[current]
                count += 1 

            #Update maximum length.
            max_len = max(count, max_len)
        return max_len
        