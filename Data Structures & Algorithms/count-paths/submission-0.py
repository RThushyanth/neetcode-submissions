class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        path_dict = {}

        for i in range(0,n):
            for j in range(0,m):
                temp_sum = 0

                if (i-1,j) in path_dict:
                    temp_sum += path_dict[(i-1,j)]
                if (i,j-1) in path_dict:
                    temp_sum += path_dict[(i,j-1)]

                if (i,j) != (0,0):
                    path_dict[(i,j)] = temp_sum
                else:
                    path_dict[(i,j)] = 1


        return path_dict[(n-1,m-1)]