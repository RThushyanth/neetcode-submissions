class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(i,j):

            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            count = 0

            if i != 0:
                count = count + dfs(i-1,j)
            if j != 0:
                count = count + dfs(i,j-1)
            if i != len(grid)-1:
                count = count + dfs(i+1,j)
            if j != len(grid[0])-1:
                count = count + dfs(i,j+1)
            
            return 1 + count

        maxarea = 0

        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 1:
                    temp = dfs(i,j)
                    if temp > maxarea:
                        maxarea = temp
        
        return maxarea
        