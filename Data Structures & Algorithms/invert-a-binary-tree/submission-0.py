# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
            
        stack = []
        stack.append(root)

        while stack:
            curr = stack.pop()
            (curr.left,curr.right) = (curr.right,curr.left)
            if curr.left != None:
                stack.append(curr.left)
            if curr.right != None:
                stack.append(curr.right)

        return root

            

        