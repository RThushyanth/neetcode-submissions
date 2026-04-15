class Solution:
    

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numset = set(nums)
        
        def getindex(y,start):
            for i in range(start,len(nums)):
                if nums[i] == y:
                    return i
            return -1

        if target%2 == 0:
            Left = int(target/2)
            Right = int(target/2)
            count = 0
            for i in range(0,len(nums)):
                if Left not in numset:
                    break
                if nums[i] == Left:
                    count = count + 1
            if count > 1:
                    return sorted([getindex(Left,0),getindex(Right,getindex(Left,0)+1)])
            else:
                Left = Left -1 
                Right = Right + 1
                while True:
                    if Left in numset and Right in numset:
                        return sorted([getindex(Left,0),getindex(Right,0)])
                    else:
                        Left = Left - 1
                        Right = Right + 1
        
        else:
            Left = target//2
            Right = target//2 + 1

            while True:
                if Left in numset and Right in numset:
                    return sorted([getindex(Left,0),getindex(Right,0)])
                else:
                    Left = Left - 1
                    Right = Right + 1

                    

        
        

        
        
        
        


        

        

            
        
        