# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return "rootnone"

        stack = []
        stack.append(root)

        data = ""

        while stack:
            curr = stack.pop()
            if curr == "lNone" or curr == "rNone":
                data = data + curr + ","
                continue
            data = data + str(curr.val) + ","
            if curr.left == None and curr.right == None:
                stack.append("rNone")
                stack.append("lNone")
            elif curr.left != None and curr.right != None:
                stack.append(curr.right)
                stack.append(curr.left)
            elif curr.right != None:
                stack.append(curr.right)
                stack.append("lNone")
            elif curr.left != None:
                stack.append("rNone")
                stack.append(curr.left)
        
        return data[0:len(data)-1]

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if data == "rootnone":
            return None

        from collections import deque

        L = deque(data.split(","))
        fval = L.popleft()
        head = TreeNode(int(fval))
        fstn = False

        stack = []
        stack.append(head)

        while L:
            cval = L.popleft()
            if cval == "lNone":
                while True:
                    cval = L.popleft()
                    if cval == "rNone":
                        stack.pop()
                        if stack == []:
                            break
                    else:
                        rNode = TreeNode(int(cval))
                        temp = stack.pop()
                        temp.right = rNode
                        stack.append(rNode)
                        break
            else:
                lNode = TreeNode(int(cval))
                temp = stack.pop()
                temp.left = lNode
                stack.append(temp)
                stack.append(lNode)

        return head
            



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))