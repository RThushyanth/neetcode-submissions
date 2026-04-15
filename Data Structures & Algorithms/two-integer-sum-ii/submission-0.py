class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers)-1

        while i<=j:
            if numbers[j] == target-numbers[i]:
                return [i+1,j+1]
            elif numbers[j] < target-numbers[i]:
                i = i + 1
            else:
                j = j-1
                
