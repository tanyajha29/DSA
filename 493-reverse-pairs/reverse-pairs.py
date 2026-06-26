class Solution(object):
    def reversePairs(self, nums):

        # count reverse pairs
        def count_pair(nums, low, mid, high):
            count = 0
            right = mid + 1

            for i in range(low, mid + 1):
                while right <= high and nums[i] > 2 * nums[right]:
                    right += 1

                count += right - (mid + 1)

            return count

        # merge function
        def merge(nums, low, mid, high):
            temp = []

            left = low
            right = mid + 1

            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1

            while left <= mid:
                temp.append(nums[left])
                left += 1

            while right <= high:
                temp.append(nums[right])
                right += 1

            for i in range(low, high + 1):
                nums[i] = temp[i - low]

        # divide and recursive calls
        def mergesort(nums, low, high):

            if low >= high:
                return 0

            mid = (low + high) // 2

            count = mergesort(nums, low, mid)
            count += mergesort(nums, mid + 1, high)

            count += count_pair(nums, low, mid, high)

            merge(nums, low, mid, high)

            return count

        return mergesort(nums, 0, len(nums) - 1)