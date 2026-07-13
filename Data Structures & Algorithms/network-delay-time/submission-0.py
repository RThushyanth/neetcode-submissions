class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        conn_dict = {}

        for tup in times:
            if tup[0] not in conn_dict:
                conn_dict[tup[0]] = {}
                conn_dict[tup[0]][tup[1]] = tup[2]
            else:
                conn_dict[tup[0]][tup[1]] = tup[2]


        visited_set = set()
        visited_set.add(k)
        
        temp_list = []
        nnode = None
        time = None
        temp_set = set()
        ans = 0

        while len(visited_set) != n:
            for node in visited_set:
                if node in conn_dict:
                    for key in list(conn_dict[node]):
                        if key in visited_set:
                            del conn_dict[node][key]
                        else:
                            temp_list.append((conn_dict[node][key],key))

            if temp_list == []:
                return -1

            nnode = min(temp_list)
            temp_list = []
            time = nnode[0]
            temp_set.add(nnode[1])
            ans = ans + time

            for node in visited_set:
                if node in conn_dict:
                    for key in list(conn_dict[node]):
                        if conn_dict[node][key] == time:
                            temp_set.add(key)
                            del conn_dict[node][key]
                        else:
                            conn_dict[node][key] = conn_dict[node][key] - time

            visited_set = visited_set.union(temp_set)
            temp_set.clear()

        return ans
            
            
            



            
            
        