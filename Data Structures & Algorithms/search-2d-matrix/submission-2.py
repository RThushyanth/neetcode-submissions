class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix) == 0:
            return False

        right = len(matrix) - 1
        left = 0
        index = 0

        while True:
            mid = (right+left)//2

            if right == left:
                index = left
                break

            if abs(right-left) == 1:
                
                if matrix[left][0] > target:
                    return False
                elif matrix[right][-1] < target:
                    return False
                elif matrix[right][0] <= target:
                    index = right
                    break
                elif matrix[left][-1] >= target:
                    index = left
                    break


            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                index = mid
                break
        
        right = len(matrix[index]) - 1
        left = 0

        while True:
            mid = (right+left)//2
            
            if right == left:
                if matrix[index][left] == target:
                    return True
                else:
                    return False
            
            if abs(right-left) == 1:
                if matrix[index][left] == target or matrix[index][right] == target:
                    return True
                else:
                    return False
            
            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
            


        