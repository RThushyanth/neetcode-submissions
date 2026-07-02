class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) == 0 or len(cost) == 1:
            return 0

        ci2 = cost[0]
        ci1 = cost[1]
        ci = 0

        for i in range(2,len(cost)):
            ci = min(ci1,ci2) + cost[i]
            ci2 = ci1
            ci1 = ci

        return min(ci1,ci2)

        