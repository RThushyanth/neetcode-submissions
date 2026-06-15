class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ret = []
        ind_dict = {}

        for i in range(0,len(nums)):
            ret.append([nums[i]])
            ind_dict[nums[i]] = i

        if len(nums) == 1:
            ret.append([])
            return ret

        

        pbl = 0
        pbr = len(nums)-1

        while len(ret[pbl]) < len(nums):
            count = 0
            for i in range(pbl,pbr+1):
                righti = ind_dict[ret[i][-1]]
                if righti != len(nums)-1:
                    for j in range(righti+1,len(nums)):
                        ret.append(ret[i] + [nums[j]])
                        count = count + 1
            pbl = pbr + 1
            pbr = pbr + count
            count = 0

        ret.append([])
        return ret



        