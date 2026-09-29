class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        dp = list(range(n + 1))
        
        for i in range(1, m + 1):
            prev_diagonal = dp[0]
            
            dp[0] = i
            
            for j in range(1, n + 1):
                temp = dp[j] 
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev_diagonal
                else:
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev_diagonal)
                
                prev_diagonal = temp
                
        return dp[n]