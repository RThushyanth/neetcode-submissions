class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        
        dp = [[0]*len(matrix[0]) for _ in range(0,len(matrix))]
        
        maxdp = 0
        
        def dfs(i,j):
            nonlocal maxdp
            curr = matrix[i][j]
            L = [1]
            if i != 0 and matrix[i-1][j] > curr:
                if dp[i-1][j] == 0:
                    L.append(dfs(i-1,j))
                else:
                    L.append(dp[i-1][j])
                    
            if j != 0 and matrix[i][j-1] > curr:
                if dp[i][j-1] == 0:
                    L.append(dfs(i,j-1))
                else:
                    L.append(dp[i][j-1])
   
            if i != len(matrix)-1 and matrix[i+1][j] > curr:
                if dp[i+1][j] == 0:
                    L.append(dfs(i+1,j))
                else:
                    L.append(dp[i+1][j])
            if j != len(matrix[0])-1 and matrix[i][j+1] > curr:
                if dp[i][j+1] == 0:
                    L.append(dfs(i,j+1))
                else:
                    L.append(dp[i][j+1])
            
            if L == [1]:
                dp[i][j] = 1
                if dp[i][j] > maxdp:
                    maxdp = dp[i][j]
                return 1
            else:
                dp[i][j] = 1+max(L)
                if dp[i][j] > maxdp:
                    maxdp = dp[i][j]
                
            
     
            return 1 + max(L)
            
               
                
        
        for i in range(0,len(matrix)):
            for j in range(0, len(matrix[0])):
                if dp[i][j] == 0:
                    dfs(i,j)
                
        
        return maxdp