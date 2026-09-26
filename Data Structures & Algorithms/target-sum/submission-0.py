class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        if target > sum(nums) or target < -1*sum(nums):
            return 0

        L =  [0]*(2*sum(nums)+1)

        L[-1] = 1

        for num in nums:
            temp_L = [0]*(2*sum(nums)+1)
            for i in range(2*num,len(L)):
                j = len(L) - 1 - i
                temp_L[j] = L[j+2*num]

            for k in range(0,len(L)):
                L[k] += temp_L[k]

        ans = 0

        try:
            ans = L[sum(nums)+target]  
        except IndexError:
            return ans
        else:
            return ans


        