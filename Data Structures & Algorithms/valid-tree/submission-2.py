class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if edges == []:
            return True

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
        no_edges = len(edges)

        def dfs(node):

            for child in nodes_dict[node]:
                if child not in visited:
                    visited[child] = 1
                    dfs(child)

            return None

        visited[0] = 1
        dfs(0)

        if len(visited) == n and no_edges == n-1:
            return True
        else:
            return False

             
        




        