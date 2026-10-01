class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        c_sum = 0
        c_l = 0

        for i in range(-len(gas),len(gas)-1,1):
            c_cost = gas[i] - cost[i]

            if c_sum > 0:
                c_sum += c_cost
                c_l += 1

            else:
                c_sum = c_cost
                c_l = 1

            if c_l == len(gas) and c_sum >= 0:
                return i+1

        return -1
        

