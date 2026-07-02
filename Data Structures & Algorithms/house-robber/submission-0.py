class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        rob3 = 0
        rob2 = nums[0]
        rob1 = nums[1]


        for i in range(2,len(nums)):
            robi = nums[i] + max(rob2,rob3)
            rob3 = rob2
            rob2 = rob1
            rob1 = robi

        return max(rob1,rob2)
        