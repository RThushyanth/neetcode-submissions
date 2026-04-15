class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        dict_nums = {}
        for i in range(0,len(nums)):
            try:
                dict_nums[nums[i]]
            except KeyError:
                dict_nums[nums[i]] = 1
            else:
                dict_nums[nums[i]] = dict_nums[nums[i]] + 1
        
        from collections import deque
        keys = list(dict_nums.keys())
        dict_cons = {}
        j = 0
        dict_cons[0] = deque([keys[0]])
        del dict_nums[keys[0]]
        forward = "Yes"
        backward = "Yes"
        while len(dict_nums) != 0:
            if forward == "Yes":
                try:
                    dict_nums[dict_cons[j][-1]+1]
                except KeyError:
                    forward = "No"
                else:
                    dict_cons[j].append(dict_cons[j][-1]+1)
                    del dict_nums[dict_cons[j][-1]]
            if backward == "Yes":
                try: 
                    dict_nums[dict_cons[j][0]-1]
                except KeyError:
                    backward = "No"
                else:
                    dict_cons[j].appendleft(dict_cons[j][0]-1)
                    del dict_nums[dict_cons[j][0]]
            if backward == "No" and forward == "No":
                j = j+1
                keys = list(dict_nums.keys())
                dict_cons[j] = deque([keys[0]])
                del dict_nums[keys[0]]
                forward = "Yes"
                backward = "Yes"

        L_lengths = []
        for i in range(0,len(dict_cons)):
            L_lengths.append(len(dict_cons[i]))
        
        return max(L_lengths)



           
            

        