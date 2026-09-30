class Solution:
    def canJump(self, nums: list[int]) -> bool:

        w_l = nums[0]

        for i in range(1,len(nums)):

            if w_l:
                w_l -= 1
                if nums[i] > w_l:
                    w_l = nums[i]
            
            else:
                return False

        return True
        