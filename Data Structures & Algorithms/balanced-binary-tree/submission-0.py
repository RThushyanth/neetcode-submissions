# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True
        if root.left == None and root.right == None:
            return True

        dnode = {}

        def treeheights(tnode):
            if tnode.left == None and tnode.right == None:
                dnode[tnode] = [0,0]
                return 0
            elif tnode.left != None and tnode.right != None:
                dnode[tnode] = [1+treeheights(tnode.left),1+treeheights(tnode.right)]
                return max(dnode[tnode][0],dnode[tnode][1])
            elif tnode.right == None:
                dnode[tnode] = [1+treeheights(tnode.left),0]
                return dnode[tnode][0]
            elif tnode.left == None:
                dnode[tnode] = [0,1+treeheights(tnode.right)]
                return dnode[tnode][1]

        treeheights(root)

        heights = list(dnode.values())

        for i in range(0,len(heights)):
            if abs(heights[i][0]-heights[i][1]) > 1:
                return False
        
        return True


            





        