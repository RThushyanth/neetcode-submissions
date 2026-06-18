class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        square = [["."] * n for _ in range(n)]
        ans = []


        def qperms(i):
            if i == n:
                tempsq = []
                for i in range(0,n):
                    temprow = "".join(square[i])
                    tempsq.append(temprow)
                ans.append(tempsq)
                return None

                
            for j in range(0,len(dsq[i])):
                if dsq[i][j] == 1:
                    ci = i
                    cj = j
                    square[ci][cj] = "Q"
                    while i+1 < n and j+1 < n:
                        dsq[i+1][j+1] = dsq[i+1][j+1] - 1
                        i = i+1
                        j = j+1
                    i = ci
                    j = cj
                    while i+1 < n and j-1 >= 0:
                        dsq[i+1][j-1] = dsq[i+1][j-1] - 1
                        i = i+1
                        j = j-1
                    i = ci
                    j = cj
                    while i+1 < n:
                        dsq[i+1][j] = dsq[i+1][j] - 1
                        i = i+1
                    i = ci
                    j = cj 
                    qperms(ci+1)
                    square[ci][cj] = "."
                    while i+1 < n and j+1 < n:
                        dsq[i+1][j+1] = dsq[i+1][j+1] + 1
                        i = i+1
                        j = j+1
                    i = ci
                    j = cj
                    while i+1 < n and j-1 >= 0:
                        dsq[i+1][j-1] = dsq[i+1][j-1] + 1
                        i = i+1
                        j = j-1
                    i = ci
                    j = cj
                    while i+1 < n:
                        dsq[i+1][j] = dsq[i+1][j] + 1
                        i = i+1
                    i = ci
                    j = cj 
            
            return None

        dsq = [[1] * n for _ in range(n)]
        qperms(0)

        return ans


        