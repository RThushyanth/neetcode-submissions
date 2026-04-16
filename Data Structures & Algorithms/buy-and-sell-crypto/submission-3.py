class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left_pointer = 0
        right_pointer = 0
        curr_lowest = 0
        curr_highest = 0

        for i in range(1,len(prices)):
            if prices[i] < prices[curr_lowest]:
                curr_lowest = i
            
            if prices[i]-prices[curr_lowest] >= prices[right_pointer]-prices[left_pointer]:
                curr_highest = i


            if curr_lowest < curr_highest:
                left_pointer = curr_lowest
                right_pointer = curr_highest
        
        return prices[right_pointer]-prices[left_pointer]
            
                
