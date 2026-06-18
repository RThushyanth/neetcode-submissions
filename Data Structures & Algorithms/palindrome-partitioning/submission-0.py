class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def checkpal(arr):
            l = 0


        ans = []

        def palcombs(i,carr):

            if i == len(s):
                ans.append(carr)

            for j in range(i,len(s)):
                k = i
                l = j
                ispal = True
                while k <= l:
                    if s[k] != s[l]:
                        ispal = False
                        break
                    k = k + 1
                    l = l - 1
                if ispal:
                    ncarr = carr + [s[i:j+1]]
                    palcombs(j+1,ncarr)

            return None

        palcombs(0,[])


        return ans