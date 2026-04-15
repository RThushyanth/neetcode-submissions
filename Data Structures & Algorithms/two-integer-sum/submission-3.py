class Solution:
    

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numdict = {}

        for i in range(0,len(nums)):
            try:
                numdict[nums[i]]
            except KeyError:
                numdict[nums[i]] = 1
            else:
                numdict[nums[i]] = numdict[nums[i]] + 1
        
        def getindex(y,start):
            for i in range(start,len(nums)):
                if nums[i] == y:
                    return i
            return -1

        if target%2 == 0:
            Mid = int(target/2)
            M_i = []
            for i in range(0,len(nums)):
                if Mid not in numdict:
                    break
                if nums[i] == Mid:
                    M_i.append(i)                    
            if len(M_i) > 1:
                return [M_i[0],M_i[1]]
            else:
                for i in range(0,len(nums)):
                    numdict[nums[i]] = numdict[nums[i]] - 1
                    if (target-nums[i]) in numdict and numdict[(target-nums[i])] > 0:
                        return [i,getindex((target-nums[i]),i+1)]
        
        else:
            for i in range(0,len(nums)):
                numdict[nums[i]] = numdict[nums[i]] - 1
                if (target-nums[i]) in numdict and numdict[target-nums[i]] > 0:
                    return [i,getindex((target-nums[i]),i+1)]

        
        

        
        
        
        


        

        

            
        
        