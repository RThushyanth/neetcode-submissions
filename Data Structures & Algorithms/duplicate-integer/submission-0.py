class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_sorted = "false"
        if len(nums) >20:
            L_p = [nums[i] for i in range(0,len(nums),(len(nums)//10))]
            if L_p.sort() == L_p:
                is_sorted = "true"
        
        if is_sorted == "true":
            for i in range(1,len(nums)-1):
                if nums[i-1] == nums[i] or nums[i+1] == nums[i]:
                    return True
            else:
                return False
        
        if is_sorted == "false":
            for i in range(0,len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[j] == nums[i]:
                        return True
            else:
                return False


            
        