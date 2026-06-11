# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        class bstviolated(Exception):
            pass

        def validbst(cnode):
            if cnode.left == None and cnode.right == None:
                return cnode.val,cnode.val
            elif cnode.left != None and cnode.right != None:
                crmin,crmax = validbst(cnode.right)
                clmin,clmax = validbst(cnode.left)

                
                if clmax >= cnode.val or crmin <= cnode.val:
                    raise bstviolated("True")

                return clmin,crmax

            elif cnode.left == None:
                crmin,crmax = validbst(cnode.right)

                if cnode.val >= crmin:
                    raise bstviolated("True")
                
                return cnode.val,crmax
            
            elif cnode.right == None:
                clmin,clmax = validbst(cnode.left)

                if clmax >= cnode.val:
                    raise bstviolated("True")

                return clmin,cnode.val

        
        try:
            validbst(root)
        except bstviolated:
            return False
        else:
            return True


        