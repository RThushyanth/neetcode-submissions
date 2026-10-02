class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        if len(intervals) == 0:
            return [newInterval]

        ans = []
        new_done = False
        i = 0

        while i < len(intervals):

            if intervals[i][0] < newInterval[0] and intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])

            elif not new_done and newInterval[0] < intervals[i][0] and newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                new_done = True

            elif not new_done and newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][0]:
                ans.append([min(newInterval[0],intervals[i][0])])
                while newInterval[1] >= intervals[i][0]:
                    i += 1
                    if i == len(intervals):
                        ans[-1].append(max(newInterval[1],intervals[i-1][1]))
                        return ans
                ans[-1].append(max(newInterval[1],intervals[i-1][1]))
                new_done = True


            if new_done:
                ans.append(intervals[i])

            i += 1

        if new_done == False:
            ans.append(newInterval)

        return ans
             
            

            




                

     