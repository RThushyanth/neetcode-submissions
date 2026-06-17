class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []

        def parcombs(prevarr,i,copen,cclose):

            if i == len(prevarr):
                parc = "".join(prevarr)
                ans.append(parc)
                return None

            if copen != n:                    
                prevarr[i] = "("
                copen = copen + 1                    
                parcombs(prevarr,i+1,copen,cclose)
                copen = copen - 1
                prevarr[i] = 0
            
            
            if copen - cclose != 0:
                prevarr[i] = ")"
                cclose = cclose + 1
                parcombs(prevarr,i+1,copen,cclose)
                cclose = cclose -1
                prevarr[i] = 0

            return None
            

        arr= [0]*2*n
        parcombs(arr,0,0,0)

        return ans
        