class Solution:
    def search(self, nums: List[int], target: int) -> int:

        right = len(nums)-1
        left = 0

        while True:

            mid = (right + left)//2

            if right == left:
                if nums[left] == target:
                    return left
                    break
                else:
                    return -1
                    break
            
            if abs(right-left) == 1:
                if nums[right] == target:
                    return right
                    break
                elif nums[left] == target:
                    return left
                    break
                else:
                    return -1
                    break
            
            if nums[mid] == target:
                return mid
                break
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            




        