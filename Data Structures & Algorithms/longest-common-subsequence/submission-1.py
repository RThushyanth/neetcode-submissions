class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0]*(len(text2)+1) for _ in range(0,len(text1)+1)]

        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    grid[i][j] = grid[i-1][j-1] + 1
                else:
                    grid[i][j] = max(grid[i-1][j],grid[i][j-1])

        return grid[-1][-1]

        