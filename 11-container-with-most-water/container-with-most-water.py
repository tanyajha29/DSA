class Solution:
    def maxArea(self, height):

        #two pointers
        # 1 at beginning
        left = 0

        # 2 at end
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            #find the total area
            container_area = width * min(height[left], height[right])

            # compare and find the max area for the container
            max_area = max(max_area, container_area)

            # check the best suitable container elements
            if height[left] < height[right]:
                left += 1
            else:
                right -=1

        return max_area
