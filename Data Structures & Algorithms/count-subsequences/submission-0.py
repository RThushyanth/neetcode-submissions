class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = [0]*len(s)
        
        for k in range(len(s)-1,-1,-1):
            if s[k] == t[-1]:
                dp[k] = 1
        
        for i in range(len(t)-2,-1,-1):
            csum = 0
            
            for j in range(len(s)-1,-1,-1):
                cval = dp[j]
                dp[j] = 0
                
                if s[j] == t[i]:
                    dp[j] = csum
                    
                csum += cval
                    
        return sum(dp)
                
                
                
            
            
            
        
        