class Solution:
    def spiralOrder(self, matrix):
        left = 0
        top = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        # array to store the result
        result = []
        while top <= bottom and left <= right :
            # traverse from left to right
            for i in range(left, right + 1) :
                result.append(matrix[top][i])
            top += 1

            # traverse from top to bottom
            for j in range(top, bottom + 1) :
                
                # store
                result.append(matrix[j][right])
            right -= 1
            
            # traverse from right to left
            if top <= bottom :
                for i in range(right, left - 1, -1) :
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            #  traverse from bottom to top
            if left <= right :
                for i in range(bottom, top - 1, -1) :
                    result.append(matrix[i][left])
                left += 1

        return result

            
                
        