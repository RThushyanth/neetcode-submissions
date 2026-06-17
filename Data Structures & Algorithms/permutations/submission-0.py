class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        perms = []

        def permutations(prevarr,ref):

            if len(ref) == 0:
                perms.append(prevarr)
                return None

            for i in range(0,len(ref)):
                carr = prevarr + [ref[i]]
                narr = ref[0:i] + ref[i+1:]
                permutations(carr,narr)

            return None
  
        permutations([], nums)
        
        return perms
        