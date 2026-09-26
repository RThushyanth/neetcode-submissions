class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if s1 == "":
            if s2 == "":
                if s3 == "":
                    return True
                else:
                    return False
            else:
                if s2 == s3:
                    return True
                else:
                    return False

        if len(s1) + len(s2) != len(s3):
            return False
          

        grid = [[""]*(len(s1)+1) for _ in range(0,len(s2)+1)]
        
        grid[0][0] = True

        for i in range(0,len(s2)+1):
            for j in range(0,len(s1)+1):
                if grid[i][j] != True:
                    continue
                
                if j != len(s1) and s1[j] == s3[i+j]:
                    grid[i][j+1] = True


                if i != len(s2) and s2[i] == s3[i+j]:
                    grid[i+1][j] = True

        if grid[-1][-1] == True:
            return True
        
        return False