class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            # target found
            if nums[mid] == target:
                return mid

            # LEFT HALF SORTED
            if nums[left] <= nums[mid]:

                # target inside left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # RIGHT HALF SORTED
            else:

                # target inside right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1