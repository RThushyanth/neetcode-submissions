class Solution:
    def reverseBits(self, n: int) -> int:


        ans = 0
        count = 0
        while n != 0:
            if n%2:
                ans = ans + 2**(31-count)
            n = n//2
            count = count + 1
        
        return ans




        