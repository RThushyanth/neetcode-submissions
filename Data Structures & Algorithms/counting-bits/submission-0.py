class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = []

        ans.append(0)
        if n == 0:
            return ans

        count = 0
        c2pow = 0
        for i in range(1,n+1):
            if i == 2**count:
                c2pow = i
                count = count + 1
            ans.append(1+ans[i-c2pow])

        return ans

            
            
        