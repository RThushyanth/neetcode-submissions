class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque

        z_q = deque([])

        clncount = 0
        fo_present = False
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 2:
                    z_q.append((i,j))
                    clncount = clncount + 1
                elif grid[i][j] == 1:
                    fo_present = True

        if clncount == 0:
            if fo_present:
                return -1
            else:
                return 0

        nlncount = 0

        clevel = 1

        while z_q:

            i,j = z_q.popleft()
            clncount = clncount - 1

            if i != 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                z_q.append((i-1,j))
                nlncount = nlncount + 1
            if j != 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                z_q.append((i,j-1))
                nlncount = nlncount + 1
            if i != len(grid)-1 and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                z_q.append((i+1,j))
                nlncount = nlncount + 1
            if j != len(grid[0])-1 and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                z_q.append((i,j+1))
                nlncount = nlncount + 1

            if clncount == 0:
                clncount = nlncount
                nlncount = 0
                clevel = clevel + 1

        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return clevel-2