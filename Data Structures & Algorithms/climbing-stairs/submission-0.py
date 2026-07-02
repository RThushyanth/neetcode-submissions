class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 0:
            return 0

        ways = 0
        wn2 = 1
        wn1 = 1
        wni = 0

        for i in range(2,n+1):
            wni = wn1 + wn2
            wn2 = wn1
            wn1 = wni

        return wni


        