class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        c_max = 0
        m_max = 0
        c_n = 0

        for i in range(0,len(nums)):


            if c_max < 0 and nums[i] > 0:
                c_max = nums[i]
            else:
                c_max += nums[i]
            
            if c_max > m_max:
                m_max = c_max

            if nums[i] <= 0:
                c_n += 1

        if c_n == len(nums) or c_n == len(nums)-1:
            return max(nums)

        else:
            return m_max

        
        