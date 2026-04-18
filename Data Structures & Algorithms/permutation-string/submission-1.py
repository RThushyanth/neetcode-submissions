class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        arr = [0]*26
        left_pointer = 0
        right_pointer = len(s1) - 1
        u_bound = len(s2)-1

        for i in range(0,len(s1)):
            t = (ord(s1[i]) - 97)
            arr[t] = arr[t] + 1
        
        for i in range(0,len(s2)):
            p = (ord(s2[i]) - 97)

            if arr[p] == 0:
                while arr[p] == 0 and left_pointer < i:
                    q = (ord(s2[left_pointer])-97)
                    arr[q] = arr[q] + 1
                    left_pointer = left_pointer + 1
                    if right_pointer + 1 <= u_bound:
                        right_pointer = right_pointer + 1
                    else:
                        return False
                    
                
                if arr[p] == 0 and left_pointer == i:
                    left_pointer = left_pointer + 1
                    if right_pointer + 1 <= u_bound:
                        right_pointer = right_pointer + 1
                    else:
                        return False
                
                elif left_pointer <= i:
                    arr[p] = 0
            
            else:
                arr[p] = arr[p] - 1
                if arr[p] == 0 and i == right_pointer:
                    return True
                

                    



        