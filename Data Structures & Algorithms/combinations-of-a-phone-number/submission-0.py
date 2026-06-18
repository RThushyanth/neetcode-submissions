class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        ph_dict = {
                    2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]
                    }

        ans = []
        carr =  []

        if digits == "":
            return []


        def phonecombs(i):
            if i == len(digits):
                tempstr = "".join(carr)
                ans.append(tempstr)
                return None

            for j in range(0,len(ph_dict[int(digits[i])])):
                carr.append(ph_dict[int(digits[i])][j])
                phonecombs(i+1)
                carr.pop()

            return None
        
        phonecombs(0)

        return ans