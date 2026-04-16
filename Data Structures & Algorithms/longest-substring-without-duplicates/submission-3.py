class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0 or len(s) == 1:
            return len(s)


        left_pointer = 0
        right_pointer = 0
        sub = {}
        sub[s[0]] = [0]
        curr_dup = 1e5
        curr_len = 1

        for i in range(1,len(s)):
            try:
                sub[s[i]]
            except KeyError:
                sub[s[i]] = [i]
                right_pointer = right_pointer + 1
                if curr_dup == left_pointer:
                    if len(sub[s[left_pointer]]) == 1:
                        del sub[s[left_pointer]]
                    elif len(sub[s[left_pointer]]) == 2:
                        if sub[s[left_pointer]][0] == left_pointer:
                            sub[s[left_pointer]].pop(0)
                    left_pointer = left_pointer + 1
                    curr_dup = 1e5
                elif curr_dup != 1e5:
                    if len(sub[s[left_pointer]]) == 1:
                        del sub[s[left_pointer]]
                    elif len(sub[s[left_pointer]]) == 2:
                        if sub[s[left_pointer]][0] == left_pointer:
                            sub[s[left_pointer]].pop(0)
                    left_pointer = left_pointer + 1
                
                if curr_dup == 1e5:
                    if right_pointer - left_pointer + 1 > curr_len:
                        curr_len = right_pointer - left_pointer + 1


            else:
                right_pointer = right_pointer+1
                if len(sub[s[i]]) == 1:
                    sub[s[i]].append(i)
                elif len(sub[s[i]]) == 2:
                    sub[s[i]].pop(0)
                    sub[s[i]].append(i)
                if curr_dup == 1e5:
                    curr_dup = sub[s[i]][0]
                else: 
                    if sub[s[i]][0] > curr_dup:
                        curr_dup = sub[s[i]][0]
                     
                if curr_dup == left_pointer:
                    if len(sub[s[left_pointer]]) == 1:
                        del sub[s[left_pointer]]
                    elif len(sub[s[left_pointer]]) == 2:
                        if sub[s[left_pointer]][0] == left_pointer:
                            sub[s[left_pointer]].pop(0)
                    left_pointer = left_pointer + 1
                    curr_dup = 1e5
                elif curr_dup != 1e5:
                    if len(sub[s[left_pointer]]) == 1:
                        del sub[s[left_pointer]]
                    elif len(sub[s[left_pointer]]) == 2:
                        if sub[s[left_pointer]][0] == left_pointer:
                            sub[s[left_pointer]].pop(0)
                    left_pointer = left_pointer + 1
                                
        return curr_len
                









        