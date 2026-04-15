class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        non_zero_ranges = []
        if heights[0] !=0:
            non_zero_ranges.append(0)
        for i in range(0,len(heights)):
            if i == len(heights) -1:
                if heights[i] !=0:
                    non_zero_ranges.append(i)
                else:
                    if len(non_zero_ranges) % 2 !=0:
                        non_zero_ranges.append(i-1)
                        
            else:
                if heights[i] == 0 and heights[i+1] !=0:
                    non_zero_ranges.append(i+1)
                if heights[i] !=0 and heights[i+1] == 0:
                    non_zero_ranges.append(i)
        
        if len(non_zero_ranges) == 0:
            return 0

        L_d = [0]*len(heights)
        while non_zero_ranges:
            end = non_zero_ranges.pop()
            start = non_zero_ranges.pop()
            L_s = []
            L_s.append(start)
            for i in range(start+1,end+1):
                if heights[i] < heights[L_s[-1]]:
                    while len(L_s) != 0 and heights[i] < heights[L_s[-1]]:
                        L_d[i] = L_d[i] + 1 + L_d[L_s[-1]]
                        L_d[L_s[-1]] = L_d[L_s[-1]] + (i-L_s[-1])
                        L_s.pop()
                        
                    L_s.append(i)
                else:
                    L_s.append(i)
            
            if len(L_s) != 0:
                while L_s:
                    L_d[L_s[-1]] = L_d[L_s[-1]] + (end-L_s[-1]+1)
                    L_s.pop()
        
        Area = 0
        for i in range(0,len(heights)):
            if heights[i] * L_d[i] > Area:
                Area = heights[i] * L_d[i]
        
        return Area






            
            



        