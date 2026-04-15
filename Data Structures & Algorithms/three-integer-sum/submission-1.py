class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        if len(nums) <=2:
            return []

        L_result = []

        nums.sort()

        k = 0
        while k < len(nums):

            if (len(nums) -1 -k) < 2:
                break
            
            if k != 0 and nums[k] == nums[k-1]:
                k = k+1
                continue

            target = 0 - nums[k]
            i = k+1
            j = len(nums)-1

            while i < j:

                if i-1 != k and nums[i-1] == nums[i]:
                    i = i+1
                    continue
                if j!= len(nums)-1 and nums[j+1] == nums[j]:
                    j = j-1
                    continue

                if nums[j] == target-nums[i]:
                    L_result.append([nums[i],nums[j],nums[k]])
                    i = i+1
                    j = j-1
                    
                    
                elif nums[j] < target-nums[i]:
                    i = i + 1
                else:
                    j = j-1
            
            

            k = k + 1
            
        return L_result
        
        