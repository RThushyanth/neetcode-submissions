class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        p_ocean = {}
        a_ocean = {}
        ans = []

        def dfs(i,j,dc):

            dc[(i,j)] = 1
            celav = heights[i][j]

            if i != 0 and heights[i-1][j] >= celav:
                if (i-1,j) not in dc:
                    dfs(i-1,j,dc)
            if j != 0 and heights[i][j-1] >= celav:
                if (i,j-1) not in dc:
                    dfs(i,j-1,dc)
            if i != len(heights)-1 and heights[i+1][j] >= celav:
                if (i+1,j) not in dc:
                    dfs(i+1,j,dc)
            if j != len(heights[0])-1 and heights[i][j+1] >= celav:
                if (i,j+1) not in dc:
                    dfs(i,j+1,dc)

            return None

        for i in range(0,len(heights)):
            dfs(i,0,p_ocean)
        for j in range(0,len(heights[0])):
            dfs(0,j,p_ocean)
        for i in range(0,len(heights)):
            dfs(i,len(heights[0])-1,a_ocean)
        for j in range(0,len(heights[0])):
            dfs(len(heights)-1,j,a_ocean)

        for i in range(0,len(heights)):
            for j in range(0,len(heights[0])):
                if (i,j) in p_ocean and (i,j) in a_ocean:
                    ans.append([i,j])



        return ans

                