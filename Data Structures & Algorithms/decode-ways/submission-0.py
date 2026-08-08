class Solution:
    def numDecodings(self, s: str) -> int:

        if len(s) == 0:
            return 0

        if s[0] == "0":
            return 0

        if len(s) == 1:
            return 1

        if "00" in s:
            return 0

        l2 = 1
        l1 = 1

        for i in range(1,len(s)):

            if (int(s[i-1])*10 + int(s[i])) in range(27,100):
                if s[i] == "0":
                    return 0
                l2 = l1

            else:
                if s[i] == "0":
                    l1 = l2
                    l2 = 0
                else:
                    l1 = l1 + l2
                    l2 = l1 - l2

        return l1