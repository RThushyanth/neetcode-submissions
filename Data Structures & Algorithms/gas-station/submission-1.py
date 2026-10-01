class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        c_sum = 0
        c_l = 0

        for i in range(-len(gas),len(gas)-1,1):

            if c_sum + gas[i] - cost[i] > gas[i] - cost[i]:
                c_sum += gas[i] - cost[i]
                c_l += 1

            else:
                c_sum = gas[i] - cost[i]
                c_l = 1

            if c_l == len(gas) and c_sum >= 0:
                return i+1

        return -1
        

