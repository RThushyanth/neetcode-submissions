class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        nodes_dict = {}
        
        for pair in edges:
            try:
                nodes_dict[pair[0]]
            except KeyError:
                nodes_dict[pair[0]] = [pair[1]]
            else:
                nodes_dict[pair[0]].append(pair[1])
            
            try:
                nodes_dict[pair[1]]
            except KeyError:
                nodes_dict[pair[1]] = [pair[0]]
            else:
                nodes_dict[pair[1]].append(pair[0])

        visited = {}
        backedge = []

        def dfs(node,parent):

            for child in nodes_dict[node]:
                if child not in visited:
                    visited[child] = 1
                    dfs(child,node)
                else:
                    if child != parent:
                        if backedge == []:
                            backedge.append(node)
                            backedge.append(child)
                        return None
            
            return None
        
        visited[edges[0][0]] = None
        dfs(edges[0][0],None)


        new_l = []
        for t in nodes_dict[backedge[1]]:
            if t != backedge[0]:
                new_l.append(t)
        nodes_dict[backedge[1]] = new_l[:]

        new_l = []
        for t in nodes_dict[backedge[0]]:
            if t != backedge[1]:
                new_l.append(t)
        nodes_dict[backedge[0]] = new_l[:]

        cycle = set()


        def dfssearch(start,stop,parent):

            if start == stop:
                return True

            for child in nodes_dict[start]:
                if child != parent:
                    if dfssearch(child,stop,start):
                        cycle.add((child,start))
                        cycle.add((start,child))
                        return True

            return None

        dfssearch(backedge[1],backedge[0],None)

        cycle.add((backedge[0],backedge[1]))
        cycle.add((backedge[1],backedge[0]))

        ans = []

        for pair in edges:
            if (pair[0],pair[1]) in cycle:
                ans = pair

        return ans






                

        