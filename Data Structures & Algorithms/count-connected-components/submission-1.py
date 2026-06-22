class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if edges == []:
            return 0

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

        for i in range(0,n):
            if i not in nodes_dict:
                nodes_dict[i] = []


        visited = {}

        def dfs(node):

            for child in nodes_dict[node]:
                if child not in visited:
                    visited[child] = 1
                    dfs(child)

            return None

        no_comp = 0

        for node in nodes_dict:
            if node not in visited:
                visited[node] = 1
                dfs(node)
                no_comp = no_comp + 1

        return no_comp
