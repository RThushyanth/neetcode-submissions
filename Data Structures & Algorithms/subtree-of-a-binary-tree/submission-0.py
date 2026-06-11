# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def vallist(rnode):
            if rnode.left == None and rnode.right == None:
                return [rnode.val,None,None]
            elif rnode.left != None and rnode.right != None:
                return [rnode.val] + vallist(rnode.left) + vallist(rnode.right)
            elif rnode.left == None:
                return [rnode.val] + [None] + vallist(rnode.right) 
            elif rnode.right == None:
                return [rnode.val] + vallist(rnode.left) + [None]

        rlist = vallist(root)
        srlist = vallist(subRoot)
        srlen = len(srlist)
        rlen = len(rlist)
        left = 0
        right = 0
        point = 1

        while True:
            if left == rlen:
                return False
            if rlist[left] != srlist[0]:
                left = left + 1
            else:
                right = left + 1
                while True:
                    if rlist[right] == srlist[point]:
                        if right - left + 1 == srlen:
                            return True
                        right = right + 1
                        if right == rlen:
                            return False
                        point = point + 1
                    else:
                        point = 1
                        right = 0 
                        left = left + 1
                        break










        