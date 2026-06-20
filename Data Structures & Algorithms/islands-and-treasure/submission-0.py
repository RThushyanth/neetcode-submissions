class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        zero_dict = {}

        from collections import deque

        z_q = deque([])

        clncount = 0
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 0:
                    z_q.append((i,j))
                    clncount = clncount + 1

        nlncount = 0

        clevel = 1

        while z_q:

            i,j = z_q.popleft()
            clncount = clncount - 1

            if i != 0 and grid[i-1][j] == 2147483647:
                grid[i-1][j] = clevel
                z_q.append((i-1,j))
                nlncount = nlncount + 1
            if j != 0 and grid[i][j-1] == 2147483647:
                grid[i][j-1] = clevel
                z_q.append((i,j-1))
                nlncount = nlncount + 1
            if i != len(grid)-1 and grid[i+1][j] == 2147483647:
                grid[i+1][j] = clevel
                z_q.append((i+1,j))
                nlncount = nlncount + 1
            if j != len(grid[0])-1 and grid[i][j+1] == 2147483647:
                grid[i][j+1] = clevel
                z_q.append((i,j+1))
                nlncount = nlncount + 1

            if clncount == 0:
                clncount = nlncount
                nlncount = 0
                clevel = clevel + 1




