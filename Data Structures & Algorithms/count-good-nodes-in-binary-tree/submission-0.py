# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = []
        stack.append(root)
        parstack = []
        count = 0
        cmax = root.val
        cmaxstack = []

        while stack:
            curr = stack.pop()

            if parstack != [] and curr == parstack[-1].right:
                parstack.pop()
                cmax = cmaxstack.pop()

            if curr.val >= cmax:
                count = count + 1
                cmax = curr.val

            if curr.right != None and curr.left != None:
                parstack.append(curr)
                cmaxstack.append(cmax)
                stack.append(curr.right)
                stack.append(curr.left)
            elif curr.right != None:
                stack.append(curr.right)
            elif curr.left != None:
                stack.append(curr.left)      

        return count