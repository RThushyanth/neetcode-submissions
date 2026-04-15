class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        alphabet_dict = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 
        'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 
        'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

        dict_str = {}

        for i in range(0,len(strs)):
            L_temp = [0]*26
            for j in range(0,len(strs[i])):
                L_temp[alphabet_dict[strs[i][j]]]   =  L_temp[alphabet_dict[strs[i][j]]] + 1
            
            tuple_temp = tuple(L_temp)

            try: 
                dict_str[tuple_temp] 

            except KeyError:
                dict_str[tuple_temp] = [strs[i]]
            
            else:
                dict_str[tuple_temp].append(strs[i])

        return list(dict_str.values())

            

            

