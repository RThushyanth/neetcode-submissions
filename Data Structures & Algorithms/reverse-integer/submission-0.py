class Solution:
    def reverse(self, x: int) -> int:
        mini = -1* 2**31
        maxi = 2**31 - 1

        if x < 0:
            sign = -1
        else:
            sign = 1
        
        rev_x = int(str(abs(x))[::-1])*sign

        if rev_x > maxi or rev_x < mini:
            return 0

        return rev_x

        