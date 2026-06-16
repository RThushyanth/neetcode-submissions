class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if min(candidates) > target:
            return []
            
        candidates.sort()
            
        ans = []
        
        def combinations(i,prevarr,ref):
            
            for j in range (i,len(ref)):
                if j != i and candidates[j] == candidates[j-1]:
                    continue
                carr = prevarr + [candidates[j]]
                csum = sum(carr)
                
                if j == len(ref)-1:
                    if csum == target:
                        ans.append(carr)
                    return None
               
                if csum == target:
                    ans.append(carr)
                    break
                elif csum > target:
                    break
                else:
                    combinations(j+1,carr, candidates)
             
            return None
           
  
        combinations(0, [], candidates)
        
        return ans