class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        i = 0
        j = len(height) - 1
        L_pointer = i
        R_pointer = j
        area = min(height[i],height[j])*(j-i)

        while i < j:
            if height[i] <= height[j]:
                while height[i] <= height[j]:
                    if i >= j:
                        break
                    if (height[i])*(j-i) >= area:
                        area = (height[i])*(j-i)
                    i = i+1
            if height[j] < height[i]:
                while height[j] < height[i]:
                    if i>= j:
                        break
                    if (height[j])*(j-i) >= area:
                        area = (height[j])*(j-i)
                    j = j-1


        return area

