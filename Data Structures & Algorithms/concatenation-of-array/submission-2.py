class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []

        for i in range(-len(nums),len(nums),1):
            ans.append(nums[i])

        return ans
        