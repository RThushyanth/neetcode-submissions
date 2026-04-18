class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_pointer = 0
        right_pointer = 0
        mst_cmn = 0
        req_cmn_cnt = 1
        max_len = 1

        dict_freq = {}
        dict_freq[s[0]] = 1

        for i in range(1,len(s)):
            right_pointer = right_pointer + 1
            
            try:
                dict_freq[s[i]]
            except KeyError:
                dict_freq[s[i]] = 1
            else:
                dict_freq[s[i]] = dict_freq[s[i]] +1

            if dict_freq[s[i]] >= req_cmn_cnt:
                mst_cmn = i 
                req_cmn_cnt = dict_freq[s[mst_cmn]]
            
            if right_pointer - left_pointer + 1 - dict_freq[s[mst_cmn]] <= k:
                if right_pointer - left_pointer + 1 > max_len:
                    max_len = right_pointer - left_pointer + 1
                
                continue

            else:
                dict_freq[s[left_pointer]] = dict_freq[s[left_pointer]] - 1
                left_pointer = left_pointer + 1

            
        return max_len






        