class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:

        a = target[0]
        b = target[1]
        c = target[2]

        a_pos = False
        b_pos = False
        c_pos = False

        for i in range(0,len(triplets)):
            if not a_pos and triplets[i][0] - a == 0 and b - triplets[i][1] >= 0 and c - triplets[i][2] >= 0:
                a_pos = True

            if not b_pos and triplets[i][1] - b == 0 and a - triplets[i][0] >= 0 and c - triplets[i][2] >= 0:
                b_pos = True

            if not c_pos and triplets[i][2] - c == 0 and b - triplets[i][1] >= 0 and a - triplets[i][0] >= 0:
                c_pos = True

        
        if a_pos and b_pos and c_pos:
            return True

        return False