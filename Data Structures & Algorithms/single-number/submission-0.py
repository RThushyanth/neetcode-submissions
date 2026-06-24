class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        bit_arrpos = [0]*16
        bit_arrneg = [0]*16

        for i in range(0,len(nums)):
            if nums[i] >= 0:
                chosen_arr = bit_arrpos
            else:
                chosen_arr = bit_arrneg
            quo = abs(nums[i])
            j = 0
            while quo != 0:
                chosen_arr[j] = chosen_arr[j] + (quo % 2)
                quo = quo//2
                j = j + 1

        ans = 0

        for i in range(0,16):
            if bit_arrpos[i] % 2 == 0:
                bit_arrpos[i] = 0
            else:
                ans = ans + 2**i
            if bit_arrneg[i] % 2 == 0:
                bit_arrneg[i] = 0
            else: 
                ans = ans - 2**i

        return ans

