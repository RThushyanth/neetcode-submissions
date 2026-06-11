# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p == None and q == None:
            return True
        elif p == None and q != None:
            return False
        elif p != None and q == None:
            return False

        def vallist(rnode):
            if rnode.left == None and rnode.right == None:
                return [rnode.val,None,None]
            elif rnode.left != None and rnode.right != None:
                return [rnode.val] + vallist(rnode.left) + vallist(rnode.right)
            elif rnode.left == None:
                return [rnode.val] + [None] + vallist(rnode.right) 
            elif rnode.right == None:
                return [rnode.val] + vallist(rnode.left) + [None]

        lp = vallist(p)
        lq = vallist(q)

        if len(lp) != len(lq):
            return False

        for i in range(0,len(lp)):
            if lp[i] != lq[i]:
                return False

        return True






        