class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ans = max(nums)
        fpblock = None
        cpblock = 1
        curr = None

        if nums == [0]*len(nums):
            return 0

        for i in range(0,len(nums)):
            if nums[i] == 0:
                if i == 0 or nums[i-1] == 0:
                    continue
                if fpblock == None:
                    if curr > ans:
                        ans = curr
                else:
                    if curr > 0 and curr > ans:
                        ans = curr
                    elif curr < 0:
                        if curr == fpblock:
                            if curr == cpblock:
                                if curr > ans:
                                    ans = curr
                            else:
                                if int(curr/cpblock) > ans:
                                    ans = int(curr/cpblock)
                        elif int(curr/fpblock) > int(curr/cpblock) and int(curr/fpblock) > ans:
                            ans = int(curr/fpblock)
                        elif int(curr/fpblock) < int(curr/cpblock) and int(curr/cpblock) > ans:
                            ans = int(curr/cpblock)
                        elif int(curr/fpblock) == int(curr/cpblock) and int(curr/fpblock) > ans:
                            ans = int(curr/fpblock)

                fpblock = None
                cpblock = 1
                curr = None
                continue

            if curr == None:
                curr = nums[i]
            else:
                curr = curr * nums[i]    

            if nums[i] < 0:
                if fpblock == None:
                    fpblock = curr
                cpblock = 1

            if fpblock != None:
                cpblock = cpblock * nums[i]
            
        if fpblock == None:
            if curr != None and curr > ans:
                ans = curr
        else:
            if curr > 0 and curr > ans:
                ans = curr
            elif curr < 0:
                if curr == fpblock:
                    if curr == cpblock:
                        if curr > ans:
                            ans = curr
                    else:
                        if int(curr/cpblock) > ans:
                            ans = int(curr/cpblock)
                elif int(curr/fpblock) > int(curr/cpblock) and int(curr/fpblock) > ans:
                    ans = int(curr/fpblock)
                elif int(curr/fpblock) < int(curr/cpblock) and int(curr/cpblock) > ans:
                    ans = int(curr/cpblock)
                elif int(curr/fpblock) == int(curr/cpblock) and int(curr/fpblock) > ans:
                    ans = int(curr/fpblock)

        return ans