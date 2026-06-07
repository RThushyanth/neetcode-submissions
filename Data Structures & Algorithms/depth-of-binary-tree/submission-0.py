# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        from collections import deque

        l = []
        queue = deque([root])
        depth = 0

        while True:
            while queue:
                curr = queue.popleft()
                if curr.left != None:
                    l.append(curr.left)
                if curr.right != None:
                    l.append(curr.right)
            depth = depth + 1
            if l == []:
                return depth
            queue.extend(l)
            l.clear()



        