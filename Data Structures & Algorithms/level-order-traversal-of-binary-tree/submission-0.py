# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []
        
        from collections import deque

        q = deque([])
        q.append(root)

        L = []
        temp  = []
        curpop = 0
        preno = 1


        while q:
            curr = q.popleft()
            temp.append(curr.val)
            curpop = curpop + 1
            
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)

            if curpop == preno:
                L.append(temp)
                temp = []
                preno = len(q)
                curpop = 0


        return L
            



        