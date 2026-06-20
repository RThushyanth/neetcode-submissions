"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if node == None:
            return None

        visited = {}

        from collections import deque

        cloneque = deque([])
        originalque = deque([])
        originalque.append(node)
        
        root = Node(node.val,[])
        cloneque.append(root)
        visited[root.val] = root

        while originalque:
            temp = originalque.popleft()
            curr = cloneque.popleft()

            

            for nei in temp.neighbors:
                try:
                    visited[nei.val]
                except KeyError:
                    nnode = Node(nei.val,[])
                    visited[nei.val] = nnode
                    curr.neighbors.append(nnode)
                    cloneque.append(nnode)
                    originalque.append(nei)
                else:
                    curr.neighbors.append(visited[nei.val])

        return root




        



        