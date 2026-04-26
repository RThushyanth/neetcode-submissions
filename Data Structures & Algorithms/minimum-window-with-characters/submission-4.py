class Solution:
    def minWindow(self, s: str, t: str) -> str:


        if len(t) > len(s):
            return ""
        
        if len(t) == len(s) and set(t) != set(s):
            return ""

 
        dict_og  = {}

        for i in range(0,len(t)):
            try:
                dict_og[t[i]]
            except KeyError:
                dict_og[t[i]] = 1
            else:
                dict_og[t[i]] = dict_og[t[i]] + 1


        prev_left = 0
        prev_right = 0
        left_pointer = 0
        right_pointer = 0
        count = 0


        # first window
        first_val = False
        i = 0
        while True:
            if i == len(s):
                return ""
            try:
                dict_og[s[i]]
            except KeyError:
                i = i + 1
                continue
            else:
                if not first_val:
                    prev_left = i
                    first_val = True
        
                dict_og[s[i]] = dict_og[s[i]] - 1

                if dict_og[s[i]] == 0:
                    count = count + 1

                if count == len(dict_og):
                    prev_right = i
                    break

                i = i+1

        def findwindow(left,right): #input left such that it is after prev left
            i = right+1
            nonlocal count
            while True:
                if i == len(s):
                    return left_pointer,right_pointer
                try:
                    dict_og[s[i]]
                except KeyError:
                    i = i + 1
                    continue
                else:
                    dict_og[s[i]] = dict_og[s[i]] - 1

                    if dict_og[s[i]] == 0:
                        count = count + 1

                    if count == len(dict_og):
                        right = i
                        break

                    i = i+1
                    
            return left,right


        def shorten(left):  #make sure inputted left existing in dictionary and only valid window is inputted
            while True:
                try: 
                    dict_og[s[left]]
                except KeyError:
                    left = left+1
                else:
                    if dict_og[s[left]] >= 0:
                        break
                    else:
                        dict_og[s[left]] = dict_og[s[left]] + 1
                        left = left + 1

            return left

        left_pointer = shorten(prev_left)
        prev_left = left_pointer
        right_pointer = prev_right

        while True:
            if dict_og[s[prev_left]] == 0:
                count = count - 1

            dict_og[s[prev_left]] = dict_og[s[prev_left]] + 1

            while True:
                if prev_left + 1 == len(s):
                    return s[left_pointer:right_pointer+1]
                try:
                    dict_og[s[prev_left + 1]]
                except KeyError:
                    prev_left = prev_left + 1
                else:
                    prev_left = prev_left + 1
                    break

            prev_left,prev_right = findwindow(prev_left,prev_right)
            if prev_left == left_pointer and prev_right == right_pointer:
                return s[left_pointer:right_pointer+1]
            prev_left = shorten(prev_left)

            if prev_right-prev_left < right_pointer - left_pointer:
                right_pointer = prev_right
                left_pointer = prev_left
            
            


        


        

        
