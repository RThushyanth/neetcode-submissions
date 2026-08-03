class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans = s[0]

        for i in range(0,len(s)-1):
            temp = ""
            for j in range(0,len(s)):
                if s[i-j] == s[i+j+1]:
                    temp = s[i-j] + temp + s[i-j]
                else:
                    if len(temp) > len(ans):
                        ans = temp
                    break
                
                if i-j-1 < 0 :
                    if len(temp) > len(ans):
                        ans = temp
                    break

                try:
                    s[i+j+2]
                except IndexError:
                    if len(temp) > len(ans):
                        ans = temp
                    break

        for i in range(1,len(s)-1):
            temp = s[i]
            for j in range(1,len(s)):
                if s[i-j] == s[i+j]:
                    temp = s[i-j] + temp + s[i-j]
                else:
                    if len(temp) > len(ans):
                        ans = temp
                    break

                if i-j-1 < 0:
                    if len(temp) > len(ans):
                        ans = temp
                    break

                try:
                    s[i+j+1]
                except IndexError:
                    if len(temp) > len(ans):
                        ans = temp
                    break

        return ans
                

                    
