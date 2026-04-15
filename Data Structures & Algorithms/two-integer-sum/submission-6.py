class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numdict = {}

        for i in range(0, len(nums)):
            try:
                numdict[nums[i]]
            except KeyError:
                numdict[nums[i]] = [i]
            else:
                numdict[nums[i]].append(i)

        if target % 2 == 0:
            Mid = int(target / 2)
            if Mid in numdict and len(numdict[Mid]) >= 2:
                return [numdict[Mid][0],numdict[Mid][1]]
            else:
                for i in range(0, len(nums)):
                    numdict[nums[i]] = numdict[nums[i]][:-1]
                    if (target - nums[i]) in numdict and len(numdict[(target - nums[i])]) > 0:
                        return [i, numdict[(target - nums[i])][0]]

        else:
            for i in range(0, len(nums)):
                numdict[nums[i]] = numdict[nums[i]][:-1]
                if (target - nums[i]) in numdict and len(numdict[(target - nums[i])]) > 0:
                    return [i, numdict[(target - nums[i])][0]]
