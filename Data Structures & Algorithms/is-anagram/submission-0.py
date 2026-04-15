class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False

        for i in range(0,len(s)):
            try:
                s_dict[s[i]] = s_dict[s[i]] + 1
            except KeyError:
                s_dict[s[i]] = 1
            
            try:
                t_dict[t[i]] = t_dict[t[i]] + 1
            except KeyError:
                t_dict[t[i]] = 1
        
        if s_dict == t_dict:
            return True
        else:
            return False



        