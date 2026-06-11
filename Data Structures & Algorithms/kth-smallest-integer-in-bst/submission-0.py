# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def linearize(node):
            if node.left == None and node.right == None:
                return [node.val]
            elif node.left != None and node.right != None:
                return linearize(node.left) + [node.val] + linearize(node.right)
            elif node.left == None:
                return [node.val] + linearize(node.right)
            elif node.right == None:
                return linearize(node.left) + [node.val]
        
        L = linearize(root)

        return L[k-1]
        