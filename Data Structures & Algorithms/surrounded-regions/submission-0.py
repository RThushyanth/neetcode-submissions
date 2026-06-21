class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited_d = {}
        is_conq = True


        def dfs(i,j,swap,check):
            nonlocal is_conq

            visited_d[(i,j)] = 1
            board[i][j] = swap

            if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1:
                is_conq = False

            if i != 0 and board[i-1][j] == check:
                p1 = dfs(i-1,j,swap,check)
            if j != 0 and board[i][j-1] == check:
                p2 = dfs(i,j-1,swap,check)
            if i != len(board)-1 and board[i+1][j] == check:
                p3 = dfs(i+1,j,swap,check)
            if j != len(board[0])-1 and board[i][j+1] == check:
                p4 = dfs(i,j+1,swap,check)

            return None

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited_d:
                    is_conq = True
                    dfs(i,j,"C","O")
                    if is_conq:
                        dfs(i,j,"X","C")
                    else:
                        dfs(i,j,"O","C")
        