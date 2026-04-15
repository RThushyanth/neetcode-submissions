class Solution:
    def trap(self, height: List[int]) -> int:


        L_bound = -1
        Area = 0
        temp_area = 0
        dist_trav = 0
        imm_dip = -1
        rpt_index = -1
        rpt_count = 0
        last_mini_chasm = -1
        for i in range (0,len(height)):

            if i == len(height)-1:
                if L_bound != -1 and height[i] >= height[L_bound]:
                    Area = Area + temp_area
                    temp_area = 0
                    dist_trav = 0
                    continue
                elif L_bound != -1 and height[i] < height[L_bound]:
                    if height[i-1] > height[i]: #descending the mini chasm
                        temp_area = temp_area + (height[L_bound]-height[i])
                        dist_trav = dist_trav + 1
                        rpt_count = 0
                        continue

                    if height[i-1] < height[i]:
                        temp_area_r = 0
                        R_bound = i
                        j = i-1
                        while height[R_bound] > height[j]:
                            temp_area_r = temp_area_r + (height[R_bound]-height[j])
                            j = j-1
                            
                        Area = Area + temp_area_r
                        temp_area = temp_area - temp_area_r + (height[L_bound]-height[i])
                        temp_area_r = 0
                        dist_trav = dist_trav + 1
                        continue
                    
                    if height[i-1] == height[i]:
                        temp_area = temp_area + (height[L_bound]-height[i])
                        dist_trav = dist_trav + 1
                        rpt_count = rpt_count + 1
                        temp_area_r = 0
                        R_bound = (i-rpt_count)
                        j = i-1
                        while height[R_bound] > height[j]:
                            temp_area_r = temp_area_r + (height[R_bound]-height[j])
                            j = j-1
                            
                        Area = Area + temp_area_r
                        temp_area = temp_area - temp_area_r + (height[L_bound]-height[i])
                        temp_area_r = 0
                        dist_trav = dist_trav + 1
                        rpt_count = 0
                        continue
                
                elif L_bound == -1:
                    continue


            
            if L_bound == -1 and height[i] != 0 and height[i+1] < height[i]: # initializing L_bound and defining wells water stores only in wells
                L_bound = i 
                continue

            if L_bound != -1 and height[i] < height[L_bound]:  # traversing the chasms since end of chasm isn't known keep traversing till you hit a wall/bumps, small bumps are also wells               
                
                if height[i-1] > height[i]: #descending the mini chasm
                    temp_area = temp_area + (height[L_bound]-height[i])
                    dist_trav = dist_trav + 1
                    rpt_count = 0

                if height[i-1] < height[i]:
                    if height[i+1] < height[i]:
                        temp_area_r = 0
                        R_bound = i
                        j = i-1
                        while height[R_bound] > height[j]:
                            temp_area_r = temp_area_r + (height[R_bound]-height[j])
                            j = j-1
                        
                        Area = Area + temp_area_r
                        temp_area = temp_area - temp_area_r + (height[L_bound]-height[i])
                        temp_area_r = 0
                        dist_trav = dist_trav + 1
                    if height[i+1] > height[i]:
                        temp_area = temp_area + (height[L_bound]-height[i])
                        dist_trav = dist_trav + 1
                        rpt_count = 0
                    continue
                    
                if height[i-1] == height[i]:
                    temp_area = temp_area + (height[L_bound]-height[i])
                    dist_trav = dist_trav + 1
                    rpt_count = rpt_count + 1
                    if height[i+1] < height[i]:
                        temp_area_r = 0
                        R_bound = (i-rpt_count)
                        j = i-1
                        while height[R_bound] > height[j]:
                            temp_area_r = temp_area_r + (height[R_bound]-height[j])
                            j = j-1
                        
                        Area = Area + temp_area_r
                        temp_area = temp_area - temp_area_r + (height[L_bound]-height[i])
                        temp_area_r = 0
                        dist_trav = dist_trav + 1
                        rpt_count = 0
                    if height[i+1] > height[i]:
                        rpt_count = 0
                    continue
            
            if L_bound != -1 and height[i] >= height[L_bound]: #end of chasm
                Area = Area + temp_area
                temp_area = 0
                dist_trav = 0
                if height[i+1] < height[i]:
                    L_bound = i
                else:
                    L_bound = -1
                continue





                
     
        return Area
                

