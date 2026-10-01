class Solution:
    def jump(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return 0

        cw = nums[0]
        nw = 0
        count = 1

        for i in range(1,len(nums)-1):

            nw -= 1
            if nums[i] > nw:
                nw = nums[i]

            cw -= 1

            if cw == 0:
                cw = nw
                nw = 0
                count += 1

        return count
        