class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        rob3 = 0
        rob2 = nums[0]
        rob1 = nums[1]


        for i in range(2,len(nums)-1):
            robi = nums[i] + max(rob2,rob3)
            rob3 = rob2
            rob2 = rob1
            rob1 = robi

        r1 = max(rob1,rob2)

        if len(nums) == 2:
            return r1

        rob3 = 0
        rob2 = nums[1]
        rob1 = nums[2]


        for i in range(3,len(nums)):
            robi = nums[i] + max(rob2,rob3)
            rob3 = rob2
            rob2 = rob1
            rob1 = robi

        r2 = max(rob1,rob2)

        return max(r1,r2)