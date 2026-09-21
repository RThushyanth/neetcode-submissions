class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        L = set()
        total_sum = sum(nums)

        if nums[-1]*2 < total_sum: 
            L.add(nums[-1])
        if nums[-1]*2 == total_sum:
            return True
        L.add(0)

        for i in range(1,len(nums)):
            j = len(nums) - 1 - i
            temp_L = []
            for k in L:
                temp_sum = k + nums[j]
                if 2*temp_sum == total_sum:
                    return True
                elif 2*temp_sum < total_sum and temp_sum not in L:
                    temp_L.append(temp_sum)
            L.update(temp_L)


        return False


        