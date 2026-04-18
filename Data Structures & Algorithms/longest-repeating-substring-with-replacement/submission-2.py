class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_pointer = 0
        right_pointer = 0
        mst_cmn = 0
        req_cmn_cnt = 1
        max_len = 1
        curr_len = 1

        dict_freq = {}
        dict_freq[s[0]] = 1

        for i in range(1,len(s)):
            right_pointer = right_pointer + 1
            
            try:
                t = dict_freq[s[i]]
            except KeyError:
                dict_freq[s[i]] = 1
            else:
                dict_freq[s[i]] = t + 1

            if dict_freq[s[i]] >= req_cmn_cnt:
                mst_cmn = i 
                req_cmn_cnt = dict_freq[s[mst_cmn]]
            
            curr_len = right_pointer - left_pointer + 1

            if curr_len - dict_freq[s[mst_cmn]] <= k:
                if curr_len > max_len:
                    max_len = curr_len
                continue

            else:
                p = dict_freq[s[left_pointer]] 
                dict_freq[s[left_pointer]] = p - 1
                left_pointer = left_pointer + 1
                if p == 0:
                    del dict[s[left_pointer-1]]


            
        return max_len






        