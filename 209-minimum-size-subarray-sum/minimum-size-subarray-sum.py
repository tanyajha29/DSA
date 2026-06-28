class Solution(object):

    def minSubArrayLen(self, target, nums):

        left = 0
        curr_sum = 0

        min_len = float('inf')

        for right in range(len(nums)):

            # add current element
            curr_sum += nums[right]

            # shrink window
            while curr_sum >= target:

                min_len = min(right - left + 1, min_len)

                curr_sum -= nums[left]

                left += 1

        if min_len == float('inf'):
            return 0

        return min_len