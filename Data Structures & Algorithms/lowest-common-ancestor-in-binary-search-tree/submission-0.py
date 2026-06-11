# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        curr = root

        if q.val > p.val:
            p,q = q,p

        while True:
            cval = curr.val
            pval = p.val
            qval = q.val
            if qval < cval and pval > cval:
                return curr
            elif qval == cval or pval == cval:
                return curr
            elif pval < cval and qval < cval:
                curr = curr.left
            elif pval > cval and qval > cval:
                curr = curr.right
        