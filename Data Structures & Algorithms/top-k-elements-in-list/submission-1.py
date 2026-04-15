class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict_freq = {}

        for i in range(0,len(nums)):
            try:
                dict_freq[nums[i]]
            except KeyError:
                dict_freq[nums[i]] = 1
            else:
                dict_freq[nums[i]] = dict_freq[nums[i]] + 1
        

        list_items = list(dict_freq.items())

        dict_rev = {}

        for i in range(0,len(list_items)):
            try:
                dict_rev[list_items[i][1]]
            except KeyError:
                dict_rev[list_items[i][1]] = [list_items[i][0]]
            else:
                dict_rev[list_items[i][1]].append(list_items[i][0])

        freq_list_1 = list(dict_rev.keys())
        freq_list = deepcopy(freq_list_1)

        def getmaxfreq(L):
            max_freq = 0
            for i in range(0,len(freq_list)):
                if freq_list[i] > max_freq:
                    max_freq = freq_list[i]
                    index = i
            freq_list[index] = 0
            return max_freq

        dict_result = {}
        lenght = 0
        for i in range(0,len(dict_rev)):
            freq = getmaxfreq(freq_list)
            dict_result[i] = dict_rev[freq]
            lenght = lenght + len(dict_rev[freq])
            if lenght == k:
                break
        L = []
        for i in range(0,len(dict_result)):
            L.extend(dict_result[i])

        return L



            





        





        
        

        



                



       

            



        