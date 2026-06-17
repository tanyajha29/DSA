class Solution(object):
    def nextPermutation(self, nums):
        index = -1
        n = len(nums)

        # Find pivot
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        # If no pivot, reverse whole array
        if index == -1:
            nums.reverse()
            return

        # Find next larger element
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        # Reverse suffix
        nums[index + 1:] = reversed(nums[index + 1:])
        