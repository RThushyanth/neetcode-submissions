class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dict_for = {}
        dict_rev = {}

        forprod = 1
        revprod = 1
        for i in range(0,len(nums)):
            j = len(nums) - 1 -i

            dict_for[i] = forprod*nums[i]
            forprod = forprod*nums[i]

            dict_rev[j] = revprod*nums[j]
            revprod = revprod*nums[j]
        
        L_result = []

        for i in range(0,len(nums)):
            if i != 0 and i!= len(nums)-1:
                L_result.append(dict_for[i-1]*dict_rev[i+1])
            elif i == len(nums)-1:
                L_result.append(dict_for[i-1])
            elif i == 0:
                L_result.append(dict_rev[i+1])
        
        return L_result
