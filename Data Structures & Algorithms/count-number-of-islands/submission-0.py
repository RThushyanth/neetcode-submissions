class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def dfs(i,j):

            if grid[i][j] == "0":
                return None

            grid[i][j] = "0"

            if i != 0:
                dfs(i-1,j)
            if j != 0:
                dfs(i,j-1)
            if i != len(grid)-1:
                dfs(i+1,j)
            if j != len(grid[0])-1:
                dfs(i,j+1)
            
            return None

        count = 0

        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count = count + 1
        
        return count
