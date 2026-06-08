# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return None

        if root.left == None and root.right == None:
            return 0

        pardict = {}

        stack = []
        parstack = []
        cdepth = 0

        if root.left != None and root.right != None:
            pardict[root] = [None,None]
            stack.append(root.left)
            stack.append(root.right)
        elif root.left == None:
            pardict[root] = [0,None]
            stack.append(root.right)
        elif root.right == None:
            pardict[root] = [None,0]
            stack.append(root.left)

        parstack.append(root)

        while stack:
            curr = stack.pop()
            cdepth = cdepth + 1

            if curr.left == None and curr.right == None:
                currpar = parstack[-1]
                if pardict[currpar][1] == None:
                    pardict[currpar] = [pardict[currpar][0],cdepth]
                else:
                    pardict[currpar] = [cdepth,pardict[currpar][1]]
                    mdepth = max(pardict[currpar])
                    parstack.pop()
                    while parstack:
                        currpar = parstack[-1]
                        if pardict[currpar][0] == None:
                            pardict[currpar] = [pardict[currpar][0],pardict[currpar][1]+mdepth]
                            break
                        else:
                            pardict[currpar] = [pardict[currpar][0]+mdepth,pardict[currpar][1]]
                            mdepth = max(pardict[currpar])
                            parstack.pop()
                if parstack == []:
                    break

                cdepth = 0

            elif curr.left != None and curr.right != None:
                lastpar = parstack[-1]
                if pardict[lastpar][1] == None:
                    pardict[lastpar] = [pardict[lastpar][0],cdepth]
                else:
                    pardict[lastpar] = [cdepth,pardict[lastpar][1]]

                parstack.append(curr)
                pardict[curr] = [None,None]
                stack.append(curr.left)
                stack.append(curr.right)
                cdepth = 0
            
            elif curr.left != None:
                stack.append(curr.left)
            else:
                stack.append(curr.right)

        edgelist = list(pardict.values())
        maxdepth = 0

        for i in range(0,len(edgelist)):
            if edgelist[i][0] + edgelist[i][1] > maxdepth:
                maxdepth = edgelist[i][0] + edgelist[i][1]
        
        return maxdepth




            
        