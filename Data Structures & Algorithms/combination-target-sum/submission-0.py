class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if min(candidates) == 2 and target == 1:
            return []

        if min(candidates) > target:
            return []

        ret = []
        ind_dict = {}
        csum_dict = {}
        ans = []

        for i in range(0,len(candidates)):
            ind_dict[candidates[i]] = i
            if candidates[i] < target:
                ret.append([candidates[i]])
                csum_dict[tuple([candidates[i]])] =candidates[i]
            elif candidates[i] == target:
                csum_dict[tuple([candidates[i]])] =candidates[i]
                ans.append([candidates[i]])

        
        pbl = 0
        pbr = len(ret)-1
        mval = min(candidates)

        while pbl < len(ret) and len(ret[pbl]) < (target//mval + 1):
            count = 0
            for i in range(pbl,pbr+1):
                righti = ind_dict[ret[i][-1]]
                csumtpl = tuple(ret[i])
                if righti != len(candidates)-1:
                    for j in range(righti,len(candidates)):
                        prcsum = csum_dict[csumtpl] + candidates[j]
                        if prcsum < target:
                            ret.append(ret[i] + [candidates[j]])
                            csum_dict[tuple(ret[-1])] = prcsum
                            count = count + 1
                        elif prcsum == target:
                            csum_dict[tuple(ret[i]+[candidates[j]])] = prcsum
                            ans.append(ret[i] + [candidates[j]])
                else:
                    prcsum = csum_dict[csumtpl] + candidates[-1]
                    if prcsum < target:
                        ret.append(ret[i]+[candidates[-1]])
                        csum_dict[tuple(ret[-1])] = prcsum
                        count = count + 1
                    elif prcsum == target:
                        csum_dict[tuple(ret[i]+[candidates[-1]])] = prcsum
                        ans.append(ret[i] + [candidates[-1]])

            pbl = pbr + 1
            pbr = pbr + count
            count = 0


        return ans


        