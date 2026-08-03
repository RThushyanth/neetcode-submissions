class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        for i in range(0,len(s)-1):
            temp = ""
            for j in range(0,len(s)):
                if s[i-j] == s[i+j+1]:
                    temp = s[i-j] + temp + s[i-j]
                    ans = ans + 1
                else:
                    break
                
                if i-j-1 < 0 :
                    break

                try:
                    s[i+j+2]
                except IndexError:
                    break

        for i in range(1,len(s)-1):
            temp = s[i]
            ans = ans + 1
            for j in range(1,len(s)):
                if s[i-j] == s[i+j]:
                    temp = s[i-j] + temp + s[i-j]
                    ans = ans + 1
                else:
                    break

                if i-j-1 < 0:
                    break

                try:
                    s[i+j+1]
                except IndexError:
                    break

        if len(s) >= 2:
            return ans + 2
        if len(s) == 1:
            return 1

