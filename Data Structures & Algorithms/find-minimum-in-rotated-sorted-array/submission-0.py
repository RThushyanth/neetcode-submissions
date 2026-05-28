class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return min(nums)

        if nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums)-1

        while True:
            mid = (left+right)//2

            if mid+1 <= right and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif mid-1 >= left and nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[left]:
                right = mid


        