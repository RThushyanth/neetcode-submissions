class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        intervals.sort()

        ans = []

        c_int = intervals[0]

        for i in range(1,len(intervals)):
            if c_int[1] >= intervals[i][0]:
                c_int[1] = max(c_int[1],intervals[i][1])
            
            else:
                ans.append(c_int)
                c_int = intervals[i]

        ans.append(c_int)

        return ans


