class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_dict = {}
        
        for word in wordDict:
            word_dict[word] = 0
        
        end_dict = {}
        expand_set = set()
        expand_set.add(0)
        temp = []

        for i in range(0,len(s)):
            temp = []
            for j in expand_set:
                if s[j:i+1] in word_dict:
                    temp.append(i+1)
            for k in temp:
                expand_set.add(k)

        if len(s) in expand_set:
            return True
        else:
            return False                