class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        if len(points) == 1:
            return [points[0]]

        import heapq

        minheap = []

        for i in range(0,len(points)):
            if len(minheap) < k:
                tpl = (-1*((points[i][0])**2 + (points[i][1])**2),points[i])
                heapq.heappush(minheap,tpl)
            else:
                if -1*((points[i][0])**2 + (points[i][1])**2) > minheap[0][0]:
                    tpl = (-1*((points[i][0])**2 + (points[i][1])**2),points[i])
                    heapq.heapreplace(minheap,tpl)
        
        L =[]
        for i in range(0,len(minheap)):
            L.append(minheap[i][1])

        return L

        