# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        from collections import deque

        preo = deque(preorder)

        inodict = {}
        preodict = {}

        nodestack = []
        root = TreeNode(preorder[0])
        nodestack.append(root)

        for i in range(0,len(inorder)):
            inodict[inorder[i]] = i
            preodict[preorder[i]] = [i]

        ltp = False
        rtp = False
        
        while preo:
            preo.popleft()
            curr = nodestack.pop()
            del preodict[curr.val]

            try:
                preodict[inorder[inodict[curr.val]-1]]
            except KeyError:
                ltp = False
            else:
                if inodict[curr.val]-1 >= 0:
                    ltp = True
                else:
                    ltp = False

            if ltp == True:
                lnode = TreeNode(preo[0])
                curr.left = lnode
                nodestack.append(curr)
                nodestack.append(lnode)
            
            else:
                while True:
                    try:
                        preodict[inorder[inodict[curr.val]+1]]
                    except KeyError:
                        rtp = False
                    except IndexError:
                        rtp = False
                    else:
                        rtp = True
                    
                    if rtp == True:
                        rnode = TreeNode(preo[0])
                        curr.right = rnode
                        nodestack.append(rnode)
                        break
                    else:
                        if nodestack == []:
                            break
                        curr = nodestack.pop()

        return root
                



        



            








       





        