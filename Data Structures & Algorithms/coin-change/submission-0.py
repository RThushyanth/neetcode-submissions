class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        dict_amt = {}
        dict_amt[0] = 0

        for i in range(1,amount+1):
            dict_amt[i] = 10e7


        for i in range(0,len(coins)):
            for j in range(0,amount+1-coins[i]):
                if dict_amt[j+coins[i]] > dict_amt[j] + 1:
                    dict_amt[j+coins[i]] = dict_amt[j] + 1


        if dict_amt[amount] == 10e7:
            return -1
        else:
            return dict_amt[amount]