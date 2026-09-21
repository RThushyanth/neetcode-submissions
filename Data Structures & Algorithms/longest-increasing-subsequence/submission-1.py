
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        len_list = [1]*len(nums)
        
        for i in range(1,len(nums)):
            j = len(nums) - i - 1
            L = [1]
            
            for k in range(j+1,len(nums)):
                if nums[k] > nums[j]:
                    L.append(len_list[k]+1)
                    
            len_list[j] = max(L)
            
        return max(len_list)
