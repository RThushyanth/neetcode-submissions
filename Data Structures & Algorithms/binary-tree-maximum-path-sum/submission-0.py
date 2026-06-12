# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        mval = []

        def currmax(node):
            if node.left == None and node.right == None:
                mval.append(node.val)
                return node.val
            elif node.left != None and node.right != None:
                lmax = currmax(node.left)
                rmax = currmax(node.right)
                
                if node.val + lmax <= node.val:
                    lmax = 0
                if node.val + rmax <= node.val:
                    rmax = 0

                mval.append(lmax + rmax + node.val)
                
                return max(lmax,rmax) + node.val
            elif node.left != None:
                lmax = currmax(node.left)
                if node.val + lmax <= node.val:
                    maxval = node.val
                else:
                    maxval = node.val + lmax
                mval.append(maxval)
                return maxval
            elif node.right !=  None:
                rmax = currmax(node.right)
                if node.val + rmax <= node.val:
                    maxval = node.val
                else:
                    maxval = node.val + rmax
                mval.append(maxval)
                return maxval

        currmax(root)

        return max(mval)

            
        