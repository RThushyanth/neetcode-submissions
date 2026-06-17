class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
            
        nums.sort()
            
        ans = []
        
        def combinations(i,prevarr,ref):
            
            for j in range (i,len(ref)):
                if j != i and nums[j] == nums[j-1]:
                    continue
        
                carr = prevarr + [nums[j]]
                ans.append(carr)
                combinations(j+1,carr, nums)
             
            return None
           
  
        combinations(0, [], nums)

        ans.append([])
        
        return ans
        