class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        cost_dict = {}

        for i in range(0,len(points)):
            cost_dict[tuple(points[i])] = {}
            for j in range(0,len(points)):
                cost_dict[tuple(points[i])][tuple(points[j])] = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        
        import heapq

        visited_set = set()
        tcost = 0
        minheap = []
        minheap.append((0,tuple(points[0])))

        while len(visited_set) != len(points):
            curr = heapq.heappop(minheap)
            if curr[1] in visited_set:
                continue

            visited_set.add(curr[1])
            tcost = tcost + curr[0]

            for key in cost_dict[curr[1]]:
                heapq.heappush(minheap,(cost_dict[curr[1]][key],key))

        return tcost

        