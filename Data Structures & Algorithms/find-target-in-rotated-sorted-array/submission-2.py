class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1 

        left = 0
        right = len(nums)-1
        min_index = -1

        if nums[0] < nums[-1]:
            while True:
                mid = (right + left)//2

                if right == left:
                    if nums[left] == target:
                        return left
                    else:
                        return -1
                
                if abs(right-left) == 1:
                    if nums[right] == target:
                        return right
                    elif nums[left] == target:
                        return left
                    else:
                        return -1
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            

        while True:
            mid = (left+right)//2

            if nums[mid] > nums[mid+1]:
                min_index = mid+1
                break
            elif nums[mid] < nums[mid-1]:
                min_index = mid
                break
            elif nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[left]:
                right = mid

        if target <= nums[min_index-1] and target >= nums[0]:
            left = 0
            right = min_index-1
        elif target >= nums[min_index] and target <= nums[-1]:
            left = min_index
            right = len(nums)-1

        while True:

            mid = (right + left)//2

            if right == left:
                if nums[left] == target:
                    return left
                else:
                    return -1
            
            if abs(right-left) == 1:
                if nums[right] == target:
                    return right
                elif nums[left] == target:
                    return left
                else:
                    return -1
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1     
        